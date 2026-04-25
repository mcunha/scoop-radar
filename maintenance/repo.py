"""Functions for cloning, validating, and updating repositories."""

import concurrent.futures
import json
import os
import shutil
from datetime import datetime, timedelta

import jsonschema
import requests
import yaml
from git import Repo

import maintenance.state as state
from maintenance.api import RateLimitExceededError, fetchjson, get_headers, make_request
from maintenance.cache import upgrade_cache_entry


def is_manifest(path):
    """Check if a file path represents a valid manifest file."""
    return path.endswith(".json") or path.endswith(".yaml") or path.endswith(".yml")


def get_next_check_due(entry):
    """Calculate the next scheduled check time for a repository."""
    last_checked_str = entry.get("last_checked", "2000-01-01T00:00:00Z")
    last_checked = datetime.strptime(last_checked_str, "%Y-%m-%dT%H:%M:%SZ")
    if last_checked_str == "2000-01-01T00:00:00Z":
        return datetime(2000, 1, 1)
    if "ignored_until" in entry:
        return datetime.strptime(entry["ignored_until"], "%Y-%m-%dT%H:%M:%SZ")
    archived = entry.get("archived", False)
    disabled = entry.get("disabled", False)
    if archived or disabled:
        interval = timedelta(days=30)
    else:
        pushed_at_str = entry.get("pushed_at", "2000-01-01T00:00:00Z")
        if not pushed_at_str:
            pushed_at_str = "2000-01-01T00:00:00Z"
        pushed_at = datetime.strptime(pushed_at_str, "%Y-%m-%dT%H:%M:%SZ")
        time_since_push = datetime.now() - pushed_at
        interval_seconds = time_since_push.total_seconds() / 10
        interval_seconds = max((6 * 3600), min(((30 * 24) * 3600), interval_seconds))
        interval = timedelta(seconds=interval_seconds)
    return last_checked + interval


def validate_manifest_file(file_path, f, is_shovel_repo):
    """Validate a manifest file against the official Scoop or Shovel schema."""
    is_valid = True
    has_checkver = False
    schema_to_use = state.SHOVEL_SCHEMA if is_shovel_repo else state.SCOOP_SCHEMA
    try:
        with open(file_path, encoding="utf-8") as mf:
            if f.endswith(".json"):
                manifest_data = json.load(mf)
            else:
                manifest_data = yaml.safe_load(mf)
        if schema_to_use:
            jsonschema.validate(instance=manifest_data, schema=schema_to_use)
            has_checkver = "checkver" in manifest_data
        elif (not isinstance(manifest_data, dict)) or ("version" not in manifest_data):
            is_valid = False
        else:
            has_checkver = "checkver" in manifest_data
    except Exception:
        is_valid = False
    return (is_valid, has_checkver)


def _probe_cache_entry(repo_path, entries, cache_entry):
    import random

    from maintenance.probe import extract_urls_from_manifest, probe_url

    if not entries:
        cache_entry["probe_success_rate"] = 1.0
        cache_entry["valid_probes"] = 0
        cache_entry["total_probes"] = 0
        return

    sample_size = min(3, len(entries))
    sampled_entries = random.sample(entries, sample_size)
    total_probes = 0
    valid_probes = 0

    for entry_file in sampled_entries:
        file_path = os.path.join(repo_path, entry_file)
        if not os.path.exists(file_path):
            file_path = os.path.join(repo_path, "bucket", entry_file)

        if os.path.exists(file_path):
            try:
                with open(file_path, encoding="utf-8") as mf:
                    if entry_file.endswith(".json"):
                        manifest_data = json.load(mf)
                    else:
                        manifest_data = yaml.safe_load(mf)
                urls = extract_urls_from_manifest(manifest_data)
                if urls:
                    url_to_probe = random.choice(urls)
                    total_probes += 1
                    if probe_url(url_to_probe):
                        valid_probes += 1
            except Exception:
                pass

    cache_entry["probe_success_rate"] = valid_probes / total_probes if total_probes > 0 else 1.0
    cache_entry["valid_probes"] = valid_probes
    cache_entry["total_probes"] = total_probes


def process_repo(repofoldername, cache_entry, dir_path):
    """Process a single repository to discover and validate manifest files."""
    if state.abort_flag:
        return None
    cache_entry = upgrade_cache_entry(repofoldername, cache_entry)
    consecutive_failures = cache_entry.get("consecutive_failures", 0)
    if "ignored_until" in cache_entry:
        ignored_until = datetime.strptime(cache_entry["ignored_until"], "%Y-%m-%dT%H:%M:%SZ")
        if datetime.now() < ignored_until:
            cache_entry["last_checked"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
            return (repofoldername, cache_entry, False)
        else:
            del cache_entry["ignored_until"]
    full_name = cache_entry["full_name"]
    git_clone_url = cache_entry["git_url"]
    default_branch = cache_entry["default_branch"]
    is_shovel_repo = "shovel-bucket" in cache_entry.get("topics", [])
    repo_path = os.path.join(dir_path, "cache", repofoldername)
    entries = []
    checkver_count = 0
    is_first_time = cache_entry["last_checked"] == "2000-01-01T00:00:00Z"
    git_success = False
    if is_first_time:
        topics = cache_entry["topics"]
        is_official = (
            ("scoop-bucket" in topics) or ("shovel-bucket" in topics) or ("scoop-apps" in topics)
        )
        looks_like_bucket = is_official
        if not is_official:
            try:
                tree_url = f"https://api.github.com/repos/{full_name}/git/trees/{default_branch}"
                resp = make_request(tree_url, headers=get_headers())
                if resp.status_code == 200:
                    tree_data = resp.json().get("tree", [])
                    for item in tree_data:
                        if ((item["path"] == "bucket") and (item["type"] == "tree")) or is_manifest(
                            item["path"]
                        ):
                            looks_like_bucket = True
                            break
            except RateLimitExceededError:
                raise
        if looks_like_bucket:
            if state.abort_flag:
                return None
            try:
                Repo.clone_from(git_clone_url, repo_path, depth=1)
                git_success = True
            except Exception:
                pass
            if os.path.isdir(repo_path):
                for d in [repo_path, os.path.join(repo_path, "bucket")]:
                    if os.path.isdir(d):
                        for f in os.listdir(d):
                            file_path = os.path.join(d, f)
                            if os.path.isfile(file_path) and is_manifest(f):
                                (is_valid, has_checkver) = validate_manifest_file(
                                    file_path, f, is_shovel_repo
                                )
                                if is_valid:
                                    entries.append(f)
                                    if has_checkver:
                                        checkver_count += 1
            cache_entry["entries"] = entries
            cache_entry["checkver_count"] = checkver_count
            _probe_cache_entry(repo_path, entries, cache_entry)
            cache_entry["last_checked"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        else:
            ignored_until = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
            cache_entry["entries"] = []
            cache_entry["checkver_count"] = 0
            cache_entry["ignored_until"] = ignored_until
            cache_entry["last_checked"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
            return (repofoldername, cache_entry, True)
    else:
        if state.abort_flag:
            return None
        if os.path.isdir(repo_path):
            try:
                repo = Repo(repo_path)
                o = repo.remotes.origin
                o.pull(depth=1)
                git_success = True
            except Exception:
                pass
        else:
            try:
                Repo.clone_from(git_clone_url, repo_path, depth=1)
                git_success = True
            except Exception:
                pass
        if os.path.isdir(repo_path):
            for d in [repo_path, os.path.join(repo_path, "bucket")]:
                if os.path.isdir(d):
                    for f in os.listdir(d):
                        file_path = os.path.join(d, f)
                        if os.path.isfile(file_path) and is_manifest(f):
                            (is_valid, has_checkver) = validate_manifest_file(
                                file_path, f, is_shovel_repo
                            )
                            if is_valid:
                                entries.append(f)
                                if has_checkver:
                                    checkver_count += 1
            cache_entry["entries"] = entries
            cache_entry["checkver_count"] = checkver_count
        _probe_cache_entry(repo_path, entries, cache_entry)
        cache_entry["last_checked"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    if not git_success:
        consecutive_failures += 1
    else:
        consecutive_failures = 0
    cache_entry["consecutive_failures"] = consecutive_failures
    if consecutive_failures >= 3:
        api_url = f"https://api.github.com/repos/{full_name}"
        try:
            resp = make_request(api_url, headers=get_headers())
            if resp.status_code == 404:
                print(f"[!] Repository {full_name} returned 404. Marking for deletion.")
                if os.path.exists(repo_path):
                    shutil.rmtree(repo_path, ignore_errors=True)
                state.evicted_count += 1
                state.evicted_repos.append(
                    {
                        "full_name": full_name,
                        "evicted_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
                    }
                )
                return (repofoldername, None, True)
        except RateLimitExceededError:
            raise
        except Exception:
            pass
    return (repofoldername, cache_entry, True)


def discover_repositories(cache):
    """Search for new repositories on GitHub."""
    queries = [
        "topic:scoop-bucket",
        "topic:shovel-bucket",
        "topic:scoop-apps",
        "scoop bucket in:name,description",
        "shovel bucket in:name,description",
        "scoop apps in:name,description",
    ]

    query_index = cache.get("search_query_index", 0)
    search_page = cache.get("search_page", 1)

    if query_index >= len(queries):
        query_index = 0
        search_page = 1

    query = queries[query_index]
    search_url = f"https://api.github.com/search/repositories?q={requests.utils.quote(query)}&per_page=100&page={search_page}"

    print(f"[*] Discovery Phase: Fetching search page {search_page} for query '{query}'...")
    try:
        response_data = fetchjson(search_url)
        items = response_data.get("items", [])
        if not items:
            print("[*] Reached end of search results for this query. Advancing to next query.")
            cache["search_page"] = 1
            cache["search_query_index"] = query_index + 1
        else:
            cache["search_page"] = search_page + 1
            cache["search_query_index"] = query_index
            for item in items:
                repofoldername = item["full_name"].replace("/", "+")
                if repofoldername not in cache:
                    cache[repofoldername] = {
                        "name": item["name"],
                        "full_name": item["full_name"],
                        "git_url": item["git_url"],
                        "html_url": item["html_url"],
                        "score": float(item["score"]),
                        "default_branch": item.get("default_branch", "master"),
                        "topics": item.get("topics", []),
                        "last_checked": "2000-01-01T00:00:00Z",
                        "pushed_at": item.get("pushed_at", "2000-01-01T00:00:00Z"),
                        "archived": item.get("archived", False),
                        "disabled": item.get("disabled", False),
                        "entries": [],
                    }
                else:
                    cache[repofoldername]["score"] = float(item["score"])
                    cache[repofoldername]["topics"] = item.get("topics", [])
                    cache[repofoldername]["pushed_at"] = item.get(
                        "pushed_at", "2000-01-01T00:00:00Z"
                    )
                    cache[repofoldername]["archived"] = item.get("archived", False)
                    cache[repofoldername]["disabled"] = item.get("disabled", False)
    except RateLimitExceededError:
        print("[!] Rate limit exceeded during repository search. Skipping search this run.")
        state.abort_flag = False


def update_repositories(cache, dir_path):
    """Update existing or new repositories."""
    MAX_API_REPOS_TO_PROCESS = 60
    repo_keys = [k for k in cache.keys() if "+" in k]
    for k in repo_keys:
        cache[k] = upgrade_cache_entry(k, cache[k])
    repo_keys.sort(key=(lambda k: get_next_check_due(cache[k])))
    now = datetime.now()
    due_repos = [k for k in repo_keys if (get_next_check_due(cache[k]) <= now)]

    repos_to_process = []
    api_repos_count = 0

    for k in due_repos:
        entry = cache[k]
        is_first_time = entry["last_checked"] == "2000-01-01T00:00:00Z"
        needs_eviction_check = entry.get("consecutive_failures", 0) >= 3
        needs_api = is_first_time or needs_eviction_check

        if needs_api:
            if api_repos_count < MAX_API_REPOS_TO_PROCESS:
                repos_to_process.append(k)
                api_repos_count += 1
        else:
            repos_to_process.append(k)

    print(
        f"[*] Processing Phase: Updating {len(repos_to_process)} out of {len(repo_keys)} total known repositories ({len(due_repos)} are currently due for a check)..."
    )
    updated_count = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for repofoldername in repos_to_process:
            futures.append(
                executor.submit(process_repo, repofoldername, cache[repofoldername], dir_path)
            )
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                if result:
                    repofoldername, entry, updated = result
                    if entry is None:
                        if repofoldername in cache:
                            del cache[repofoldername]
                    else:
                        cache[repofoldername] = entry
                    if updated:
                        updated_count += 1
            except RateLimitExceededError:
                print("[!] Rate limit exception caught in thread. Shutting down pool cleanly...")
                state.abort_flag = True
    print(f"[*] Slice complete. {updated_count} repos actually updated their data/files.")
    return updated_count
