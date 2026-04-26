import argparse
import concurrent.futures
import json
import os
import shutil
import stat
import subprocess
from datetime import datetime, timedelta, timezone

from maintenance.config import get_config


def get_daily_snapshots(repo_path, full_name, is_shovel_bucket, config):
    """Get the state of the repository for the last 91 days."""
    snapshots = {}

    # Use UTC to align with our crawler logic
    today = datetime.now(timezone.utc).replace(hour=23, minute=59, second=59)
    dates = []
    for i in range(91, -1, -1):
        d = today - timedelta(days=i)
        dates.append((d, d.strftime("%Y-%m-%d")))

    for d, date_str in dates:
        git_date = d.strftime("%Y-%m-%d %H:%M:%S")
        try:
            result = subprocess.run(
                ["git", "rev-list", "-1", f"--before={git_date}", "HEAD"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True,
            )
            commit_hash = result.stdout.strip()
            if commit_hash:
                tree_result = subprocess.run(
                    ["git", "ls-tree", "-r", "--name-only", commit_hash],
                    cwd=repo_path,
                    capture_output=True,
                    text=True,
                    check=True,
                )
                files = tree_result.stdout.strip().splitlines()

                valid_files = set()
                valid_shovel = set()
                valid_scoop = set()

                for f in files:
                    if config.name == "winget":
                        # Skip multifile parts to accurately count the package identity
                        if ".installer." in f or ".locale." in f:
                            continue
                        
                        normalized_f = f.replace("\\", "/")
                        if f.endswith(".yaml") and any(d in normalized_f for d in ["manifests/", "packages/", "automatic/", "manual/"]):
                            valid_files.add(f"{full_name}:{f.split('/')[-1]}".lower())
                    else:
                        if f.endswith(".json") or f.endswith(".yaml") or f.endswith(".yml"):
                            parts = f.split("/")
                            if len(parts) == 1 or (len(parts) == 2 and parts[0] == "bucket"):
                                recipe_name = parts[-1]
                                item = f"{full_name}:{recipe_name}".lower()

                                is_shovel = (
                                    is_shovel_bucket or f.endswith(".yaml") or f.endswith(".yml")
                                )

                                valid_files.add(item)
                                if config.name == "scoop_shovel":
                                    if is_shovel:
                                        valid_shovel.add(item)
                                    else:
                                        valid_scoop.add(item)

                snapshots[date_str] = {
                    "all": valid_files,
                    "scoop": valid_scoop,
                    "shovel": valid_shovel,
                }
            else:
                snapshots[date_str] = {"all": set(), "scoop": set(), "shovel": set()}
        except subprocess.CalledProcessError:
            snapshots[date_str] = {"all": set(), "scoop": set(), "shovel": set()}

    return snapshots


def process_repository(repo, config):
    """Clone a repository and get its historical snapshots."""
    full_name = repo["full_name"]
    git_url = repo["git_url"]
    topics = repo.get("topics", [])
    is_shovel_bucket = "shovel-bucket" in topics

    repo_dir = f"temp_seed_clones/{full_name.replace('/', '+')}"

    print(f"[*] Seeding {full_name}...")

    if not os.path.exists(repo_dir):
        try:
            subprocess.run(["git", "clone", "--quiet", git_url, repo_dir], check=True)
        except subprocess.CalledProcessError:
            print(f"[!] Failed to clone {full_name}")
            return None
    else:
        try:
            subprocess.run(["git", "pull", "--quiet"], cwd=repo_dir, check=True)
        except subprocess.CalledProcessError:
            pass

    snapshots = get_daily_snapshots(repo_dir, full_name, is_shovel_bucket, config)

    try:

        def remove_readonly(func, path, _):
            os.chmod(path, stat.S_IWRITE)
            func(path)

        shutil.rmtree(repo_dir, onerror=remove_readonly)
    except Exception as e:
        print(f"[!] Failed to clean up {repo_dir}: {e}")

    return snapshots


def seed_ecosystem(ecosystem_name):
    print(f"\n{'='*50}\n[*] Starting seed generation for: {ecosystem_name}\n{'='*50}")
    config = get_config(ecosystem_name)
    json_path = os.path.join(config.out_dir, "all.json")

    if not os.path.exists(json_path):
        print(f"[!] {json_path} not found. Run the crawler first to generate the ecosystem data.")
        return

    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    repos = data.get("all", [])
    if not repos:
        print(f"[!] No repositories found in {json_path}.")
        return

    os.makedirs("temp_seed_clones", exist_ok=True)

    today = datetime.now(timezone.utc).replace(hour=23, minute=59, second=59)
    dates = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(91, -1, -1)]

    global_snapshots = {
        date_str: {"all": set(), "scoop": set(), "shovel": set()} for date_str in dates
    }

    # Process up to 10 repos concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_repo = {executor.submit(process_repository, repo, config): repo for repo in repos}

        for future in concurrent.futures.as_completed(future_to_repo):
            repo = future_to_repo[future]
            try:
                repo_snapshots = future.result()
                if repo_snapshots:
                    for date_str, snaps in repo_snapshots.items():
                        if date_str in global_snapshots:
                            global_snapshots[date_str]["all"].update(snaps["all"])
                            if config.name == "scoop_shovel":
                                global_snapshots[date_str]["scoop"].update(snaps["scoop"])
                                global_snapshots[date_str]["shovel"].update(snaps["shovel"])
            except Exception as e:
                print(f"[!] Exception processing {repo['full_name']}: {e}")

    timeseries = []

    def calc_delta(curr, prev):
        added = len(curr - prev)
        deleted = len(prev - curr)
        retained = len(curr & prev)
        return {"added": added, "deleted": -deleted, "retained": retained}

    for i in range(1, len(dates)):
        curr_date = dates[i]
        prev_date = dates[i - 1]

        curr_snap = global_snapshots[curr_date]
        prev_snap = global_snapshots[prev_date]

        daily_entry = {
            "date": curr_date,
            "all": calc_delta(curr_snap["all"], prev_snap["all"]),
        }
        if config.name == "scoop_shovel":
            daily_entry["scoop"] = calc_delta(curr_snap["scoop"], prev_snap["scoop"])
            daily_entry["shovel"] = calc_delta(curr_snap["shovel"], prev_snap["shovel"])

        timeseries.append(daily_entry)

    # Output to seed_timeseries.json in the ecosystem directory
    seed_output_path = os.path.join(config.out_dir, "seed_timeseries.json")
    with open(seed_output_path, "w", encoding="utf-8") as f:
        json.dump(timeseries, f, indent=2)

    print(
        f"[*] Seed generation complete. Timeseries rebuilt for last {len(timeseries)} days. Saved to {seed_output_path}"
    )

    try:
        os.rmdir("temp_seed_clones")
    except OSError:
        pass


def main():
    parser = argparse.ArgumentParser(description="Seed Timeseries Generator")
    parser.add_argument(
        "--ecosystem",
        type=str,
        default="all",
        choices=["all", "scoop_shovel", "chocolatey", "winget"],
        help="Which ecosystem to seed",
    )
    args = parser.parse_args()

    ecosystems_to_run = (
        ["scoop_shovel", "chocolatey", "winget"] if args.ecosystem == "all" else [args.ecosystem]
    )

    for eco in ecosystems_to_run:
        seed_ecosystem(eco)


if __name__ == "__main__":
    main()
