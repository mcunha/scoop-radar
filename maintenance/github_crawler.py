"""Github crawler for Scoop and Shovel buckets."""

import os
import time

from dotenv import load_dotenv

import maintenance.state as state
from maintenance.api import fetch_schema_with_etag
from maintenance.cache import load_cache, save_cache
from maintenance.metrics import calculate_metrics
from maintenance.output import generate_apis, generate_readme
from maintenance.repo import discover_repositories, update_repositories

dir_path = os.path.dirname(os.path.realpath(__file__))


def fetch_schemas(cache):
    """Fetch JSON schemas for Scoop and Shovel."""
    print("[*] Fetching JSON schemas for validation...")
    state.SCOOP_SCHEMA = fetch_schema_with_etag(
        "https://raw.githubusercontent.com/ScoopInstaller/Scoop/master/schema.json",
        "__scoop_schema",
        cache,
    )
    state.SHOVEL_SCHEMA = fetch_schema_with_etag(
        "https://raw.githubusercontent.com/Ash258/Scoop-Core/main/schema.json",
        "__shovel_schema",
        cache,
    )


def main():
    """Main entrypoint for the GitHub crawler process."""
    load_dotenv()
    start_time = time.time()

    os.makedirs(os.path.join(dir_path, "cache"), exist_ok=True)

    cache = load_cache(dir_path)

    fetch_schemas(cache)
    discover_start = time.time()
    discover_repositories(cache)
    discover_time = time.time() - discover_start

    update_start = time.time()
    updated_count = update_repositories(cache, dir_path)
    update_time = time.time() - update_start

    save_cache(cache, dir_path)

    actual_repos, scoop_repos, shovel_repos, trending, hidden_gems, ecosystem_metrics = (
        calculate_metrics(cache)
    )

    total_buckets = len(actual_repos)
    total_recipes = sum(len(repo.get("entries", [])) for repo in actual_repos)

    run_duration = time.time() - start_time
    global_metrics = cache.get(
        "global_metrics",
        {
            "total_runs": 0,
            "total_run_time_seconds": 0.0,
            "total_repo_updates": 0,
            "previous_total_buckets": total_buckets,
            "previous_total_recipes": total_recipes,
            "bucket_velocity": 0,
            "recipe_velocity": 0,
            "total_evictions": 0,
            "total_api_retries": 0,
        },
    )

    global_metrics["total_runs"] += 1
    global_metrics["total_run_time_seconds"] += run_duration
    # In case update_repositories returned None (e.g. abort)
    global_metrics["total_repo_updates"] += updated_count or 0

    # Velocity calculation (net new)
    global_metrics["bucket_velocity"] = total_buckets - global_metrics.get(
        "previous_total_buckets", total_buckets
    )
    global_metrics["recipe_velocity"] = total_recipes - global_metrics.get(
        "previous_total_recipes", total_recipes
    )

    global_metrics["previous_total_buckets"] = total_buckets
    global_metrics["previous_total_recipes"] = total_recipes

    global_metrics["total_evictions"] = (
        global_metrics.get("total_evictions", 0) + state.evicted_count
    )
    global_metrics["total_api_retries"] = (
        global_metrics.get("total_api_retries", 0) + state.api_retries
    )

    global_metrics["last_run_discover_time"] = discover_time
    global_metrics["last_run_update_time"] = update_time

    total_valid_probes = sum(repo.get("valid_probes", 0) for repo in actual_repos)
    total_probes = sum(repo.get("total_probes", 0) for repo in actual_repos)
    global_metrics["ecosystem_reliability"] = (
        round(total_valid_probes / total_probes * 100, 1) if total_probes > 0 else 100.0
    )

    try:
        cache_size_mb = os.path.getsize(os.path.join(dir_path, "cache.pickle")) / (1024 * 1024)
    except OSError:
        cache_size_mb = 0.0
    global_metrics["cache_size_mb"] = cache_size_mb

    # Merge ecosystem metrics into global metrics
    global_metrics.update(ecosystem_metrics)

    cache["global_metrics"] = global_metrics

    from datetime import datetime, timedelta, timezone

    # Process recent evictions (last 90 days)
    evictions = cache.get("evictions", [])
    if state.evicted_repos:
        evictions.extend(state.evicted_repos)

    cutoff_date = datetime.now(timezone.utc) - timedelta(days=90)
    recent_evictions = []
    for ev in evictions:
        try:
            ev_date = datetime.strptime(ev["evicted_at"], "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=timezone.utc
            )
            if ev_date >= cutoff_date:
                recent_evictions.append(ev)
        except (KeyError, ValueError):
            pass

    cache["evictions"] = recent_evictions

    # --- Timeseries generation for Pygal ---
    current_recipes_set = set()
    current_scoop_recipes_set = set()
    current_shovel_recipes_set = set()

    for repo in actual_repos:
        is_shovel = "shovel-bucket" in repo.get("topics", []) or any(
            e.endswith(".yaml") or e.endswith(".yml") for e in repo.get("entries", [])
        )

        for entry in repo.get("entries", []):
            entry_name = entry.split("/")[-1]
            item = f"{repo['full_name']}:{entry_name}".lower()
            current_recipes_set.add(item)
            if is_shovel:
                current_shovel_recipes_set.add(item)
            else:
                current_scoop_recipes_set.add(item)

    previous_recipes_set = set(cache.get("previous_recipes_set", current_recipes_set))
    previous_scoop_recipes_set = set(
        cache.get("previous_scoop_recipes_set", current_scoop_recipes_set)
    )
    previous_shovel_recipes_set = set(
        cache.get("previous_shovel_recipes_set", current_shovel_recipes_set)
    )

    # Prevent ecosystem spikes from newly discovered, pre-existing buckets
    previous_known_repos = set(
        cache.get("previous_known_repos", [r["full_name"] for r in actual_repos])
    )
    current_known_repos = set(repo["full_name"] for repo in actual_repos)
    newly_discovered_repos = current_known_repos - previous_known_repos
    cache["previous_known_repos"] = list(current_known_repos)

    for repo in actual_repos:
        if repo["full_name"] in newly_discovered_repos:
            is_shovel = "shovel-bucket" in repo.get("topics", []) or any(
                e.endswith(".yaml") or e.endswith(".yml") for e in repo.get("entries", [])
            )
            for entry in repo.get("entries", []):
                item = f"{repo['full_name']}:{entry}".lower()
                previous_recipes_set.add(item)
                if is_shovel:
                    previous_shovel_recipes_set.add(item)
                else:
                    previous_scoop_recipes_set.add(item)

    def calc_delta(curr, prev):
        added = len(curr - prev)
        deleted = len(prev - curr)
        retained = len(curr & prev)
        return {"added": added, "deleted": -deleted, "retained": retained}

    daily_entry = {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "all": calc_delta(current_recipes_set, previous_recipes_set),
        "scoop": calc_delta(current_scoop_recipes_set, previous_scoop_recipes_set),
        "shovel": calc_delta(current_shovel_recipes_set, previous_shovel_recipes_set),
    }

    timeseries = cache.get("timeseries_history", [])

    # Inject historical seed data if we are missing it (e.g. running in CI for the first few times)
    if len(timeseries) < 80:
        seed_path = os.path.join(dir_path, "seed_timeseries.json")
        if os.path.exists(seed_path):
            import json

            try:
                with open(seed_path, encoding="utf-8") as f:
                    seed_timeseries = json.load(f)

                # Check if timeseries already has an entry for today from earlier in the run
                if (
                    timeseries
                    and seed_timeseries
                    and seed_timeseries[-1]["date"] >= timeseries[0]["date"]
                ):
                    # Keep the seed data up until today's date
                    seed_timeseries = [
                        t for t in seed_timeseries if t["date"] < timeseries[0]["date"]
                    ]

                timeseries = seed_timeseries + timeseries
                print(
                    f"[*] Loaded {len(seed_timeseries)} days of historical timeseries data from seed."
                )
            except Exception as e:
                print(f"[!] Warning: Failed to load seed timeseries: {e}")

    if not timeseries or timeseries[-1]["date"] != daily_entry["date"]:
        timeseries.append(daily_entry)
    else:
        timeseries[-1] = daily_entry

    if len(timeseries) > 90:
        timeseries = timeseries[-90:]

    cache["timeseries_history"] = timeseries
    cache["previous_recipes_set"] = list(current_recipes_set)
    cache["previous_scoop_recipes_set"] = list(current_scoop_recipes_set)
    cache["previous_shovel_recipes_set"] = list(current_shovel_recipes_set)

    import argparse

    from maintenance.output import generate_growth_charts

    parser = argparse.ArgumentParser(description="Scoop Radar Crawler")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force writing outputs and saving cache when running locally",
    )
    args, _ = parser.parse_known_args()

    is_ci = os.environ.get("GITHUB_ACTIONS") == "true"

    if is_ci or args.force:
        out_dir = os.path.normpath(os.path.join(dir_path, ".."))
    else:
        out_dir = os.path.join(dir_path, "..", "localonly-output")
        os.makedirs(out_dir, exist_ok=True)
        print(f"\n[INFO] Running in local mode. Writing generated outputs to '{out_dir}'.")
        print("[INFO] To overwrite real repository files and cache, use --force.")

    generate_growth_charts(timeseries, out_dir)

    generate_readme(
        actual_repos,
        scoop_repos,
        shovel_repos,
        hidden_gems,
        trending,
        global_metrics,
        out_dir,
        dir_path,
    )
    generate_apis(
        actual_repos,
        scoop_repos,
        shovel_repos,
        hidden_gems,
        trending,
        recent_evictions,
        global_metrics,
        out_dir,
    )

    if is_ci or args.force:
        # Save cache AFTER all ranks and metrics have been calculated so they persist for the next run!
        save_cache(cache, dir_path)
    else:
        # Also save cache locally so we don't refetch everything constantly
        print("[INFO] Saving cache.pickle to localonly-output for debugging...")
        save_cache(cache, out_dir)

    print("[INFO] Script Finished and outputs written.")


if __name__ == "__main__":
    main()
