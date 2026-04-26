"""Functions for scoring and calculating metrics."""

import math
from datetime import datetime, timezone
from urllib.parse import urlparse

from maintenance.api import fetchjson


def extract_github_repos(url):
    """Extract GitHub repository paths from a JSON URL."""
    data = fetchjson(url)
    repos = []
    for v in data.values():
        if isinstance(v, str):
            try:
                parsed = urlparse(v)
                if parsed.netloc == "github.com" or parsed.netloc == "www.github.com":
                    path = parsed.path.lstrip("/")
                    if path.endswith(".git"):
                        path = path[:-4]
                    if path:
                        repos.append(path)
            except ValueError:
                pass
    return repos


def get_repo_score(repo, official_recipes):
    """Calculate the final score for a repository."""
    # Dilute the base GitHub search score to prevent "Star/Age Bias"
    base_score = repo.get("score", 0) * 0.5

    entries = repo.get("entries", [])
    entries_count = len(entries)

    # Logarithmic recipe scoring to prevent mega-bucket runaway
    recipe_score = math.log(entries_count + 1) * 15

    # Uniqueness factor: +2 points for each recipe NOT in official buckets
    unique_count = sum(1 for e in entries if e.lower() not in official_recipes)
    uniqueness_score = unique_count * 2

    pushed_at_str = repo.get("pushed_at", "2000-01-01T00:00:00Z")
    if not pushed_at_str:
        pushed_at_str = "2000-01-01T00:00:00Z"
    pushed_at = datetime.strptime(pushed_at_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    days_since_push = (datetime.now(timezone.utc) - pushed_at).days

    # Flatten the recency curve for the first 14 days so automated checkver bots (0 days)
    # don't get a micro-advantage over manual maintainers who batch updates weekly.
    effective_days_since_push = max(0, days_since_push - 14)

    # Up to 20 points for recency, decaying over roughly a year (365 days / 18.25 = 20)
    recency_score = max(0, 20 - (effective_days_since_push / 18.25))

    # Quality Gate: Staleness penalty scales with inactivity duration AND bucket size.
    # A massive bucket unmaintained for a long time is full of broken/insecure recipes.
    staleness_penalty = 0
    if days_since_push > 180:  # 6 months grace period before rot sets in
        months_stale = (days_since_push - 180) / 30.0
        # Larger buckets rot faster. We use logarithmic scaling to match the recipe score curve.
        rot_rate = math.log(entries_count + 2) * 2.0
        staleness_penalty = -(months_stale * rot_rate)

    # Reliability Penalty
    probe_success_rate = repo.get("probe_success_rate", 1.0)
    reliability_penalty = 0
    if probe_success_rate < 1.0:
        # If 0% success, massive penalty
        reliability_penalty = -30 * (1.0 - probe_success_rate)

    return (
        base_score
        + recipe_score
        + uniqueness_score
        + recency_score
        + staleness_penalty
        + reliability_penalty
    )


def calculate_metrics(cache, config):
    """Calculate metrics for all repositories and return categorized lists."""
    repo_keys = [k for k in cache.keys() if "+" in k]

    known_buckets = {}
    for key, url in config.known_buckets_urls.items():
        known_buckets[key] = extract_github_repos(url)

    # Build a set of official recipes for uniqueness scoring
    official_recipes = set()
    for k in repo_keys:
        repo = cache[k]
        full_name_lower = repo.get("full_name", "").lower()
        repo_org = full_name_lower.split("/")[0] if "/" in full_name_lower else ""
        if repo_org in config.official_orgs:
            for e in repo.get("entries", []):
                official_recipes.add(e.split("/")[-1].lower())

    actual_repos = [cache[repo] for repo in repo_keys if len(cache[repo].get("entries", [])) > 0]

    # Calculate uniqueness metrics for hidden gems
    for repo in actual_repos:
        entries = repo.get("entries", [])
        unique_count = sum(1 for e in entries if e.split("/")[-1].lower() not in official_recipes)
        repo["unique_count"] = unique_count
        repo["uniqueness_ratio"] = unique_count / len(entries) if entries else 0

        checkver_count = repo.get("checkver_count", 0)
        repo["auto_update_percentage"] = (
            round((checkver_count / len(entries) * 100), 2) if entries else 0.0
        )

        repo["final_score"] = get_repo_score(repo, official_recipes)

    actual_repos = sorted(actual_repos, key=lambda r: r["final_score"], reverse=True)

    # Calculate rank velocity for Trending
    for i, repo in enumerate(actual_repos):
        repo["current_rank"] = i + 1
        previous_rank = repo.get("previous_rank", repo["current_rank"])
        repo["rank_velocity"] = previous_rank - repo["current_rank"]
        # Set previous_rank for the NEXT run
        repo["previous_rank"] = repo["current_rank"]

    scoop_repos = []
    shovel_repos = []

    for repo in actual_repos:
        topics = repo.get("topics", [])
        entries = repo.get("entries", [])

        full_name_lower = repo.get("full_name", "").lower()
        repo_org = full_name_lower.split("/")[0] if "/" in full_name_lower else ""

        # For Scoop/Shovel Ecosystem compatibility, populate these specific keys.
        # For Chocolatey, they will just be false, which is fine since the templates can be updated or will just ignore them.
        repo["is_scoop_official"] = repo_org in ["scoopinstaller"] if config.name == "scoop_shovel" else (repo_org in config.official_orgs)
        repo["is_scoop_known"] = full_name_lower in [b.lower() for b in known_buckets.get("scoop", [])] if config.name == "scoop_shovel" else False

        repo["is_shovel_official"] = repo_org in ["ash258", "shovel-org"] if config.name == "scoop_shovel" else False
        repo["is_shovel_known"] = full_name_lower in [b.lower() for b in known_buckets.get("shovel", [])] if config.name == "scoop_shovel" else False

        is_shovel = "shovel-bucket" in topics or any(
            e.endswith(".yaml") or e.endswith(".yml") for e in entries
        )
        if is_shovel and config.name == "scoop_shovel":
            shovel_repos.append(repo)
        else:
            scoop_repos.append(repo)

    # Discover "Trending": active repos that moved up the most ranks recently.
    trending = [
        r
        for r in actual_repos
        if r["rank_velocity"] > 0 and r["final_score"] > 20 and len(r.get("entries", [])) >= 5
    ]
    trending = sorted(trending, key=lambda r: r["rank_velocity"], reverse=True)[:5]

    # Discover "Hidden Gems": active, high uniqueness ratio (>50%), but not necessarily top overall score.
    hidden_gems = []
    for r in actual_repos:
        pushed_at_str = r.get("pushed_at", "2000-01-01T00:00:00Z")
        pushed_at = datetime.strptime(pushed_at_str, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=timezone.utc
        )
        if (
            r["uniqueness_ratio"] >= 0.5
            and r["unique_count"] >= 5
            and (datetime.now(timezone.utc) - pushed_at).days <= 90
            and not r.get("is_scoop_official")
            and not r.get("is_scoop_known")
            and not r.get("is_shovel_official")
            and not r.get("is_shovel_known")
        ):
            hidden_gems.append(r)

    # Sort hidden gems by uniqueness ratio then final score
    hidden_gems = sorted(
        hidden_gems,
        key=lambda r: (r["uniqueness_ratio"], r["final_score"]),
        reverse=True,
    )[:10]

    # Calculate Ecosystem Health Metrics
    total_checkver_count = 0
    total_entries_count = 0
    stale_bucket_count = 0
    official_recipe_count = 0
    community_recipe_count = 0
    community_unique_recipes = set()

    for repo in actual_repos:
        entries = repo.get("entries", [])
        total_entries_count += len(entries)
        total_checkver_count += repo.get("checkver_count", 0)

        # Calculate official vs community recipe counts
        for e in entries:
            e_name = e.split("/")[-1].lower()
            if e_name in official_recipes:
                official_recipe_count += 1
            else:
                community_recipe_count += 1
                community_unique_recipes.add(e_name)

        # Count stale buckets (no push in > 365 days)
        pushed_at_str = repo.get("pushed_at", "2000-01-01T00:00:00Z")
        pushed_at = datetime.strptime(pushed_at_str, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=timezone.utc
        )
        if (datetime.now(timezone.utc) - pushed_at).days > 365:
            stale_bucket_count += 1

    total_unique_recipes = len(official_recipes) + len(community_unique_recipes)

    ecosystem_metrics = {
        "total_unique_recipes": total_unique_recipes,
        "auto_update_percentage": round((total_checkver_count / total_entries_count * 100), 2)
        if total_entries_count
        else 0.0,
        "official_recipes": official_recipe_count,
        "community_recipes": community_recipe_count,
        "stale_buckets": stale_bucket_count,
        "shovel_buckets": len(shovel_repos),
        "scoop_buckets": len(scoop_repos),
    }

    return actual_repos, scoop_repos, shovel_repos, trending, hidden_gems, ecosystem_metrics
