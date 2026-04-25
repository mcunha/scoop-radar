# scoop-radar
A data-driven, automated discovery and ranking engine for the Scoop package manager ecosystem on Windows

# Build Status
![Tests & Linting](https://github.com/mcunha/scoop-radar/actions/workflows/test.yml/badge.svg)
![Update Scoop Radar README](https://github.com/mcunha/scoop-radar/actions/workflows/update.yml/badge.svg)

# Acknowledgements
This project was heavily inspired by the original `awesome-scoop` directories maintained by [algomaniac](https://github.com/algomaniac) and [tapannallan](https://github.com/tapannallan).

# 📊 Ecosystem Health
* **Total Unique Recipes**: {{ metrics.total_unique_recipes }}
* **Ecosystem Auto-Update Health**: {{ metrics.auto_update_percentage }}%
* **Ecosystem Reliability**: {{ metrics.ecosystem_reliability }}% (Sampled URL Health)
* **Official vs. Community**: {{ metrics.official_recipes }} Official / {{ metrics.community_recipes }} Community
* **Bucket Ecosystem**: {{ metrics.scoop_buckets }} Scoop / {{ metrics.shovel_buckets }} Shovel
* **Bucket Graveyard (Stale > 1 Year)**: 🪦 {{ metrics.stale_buckets }}

### Ecosystem Growth (All Recipes)
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="growth_all_dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="growth_all_light.svg">
  <img alt="All Recipes Growth" src="growth_all_light.svg">
</picture>

### Scoop vs Shovel Growth
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="growth_scoop_dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="growth_scoop_light.svg">
    <img alt="Scoop Recipes Growth" src="growth_scoop_light.svg" width="49%">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="growth_shovel_dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="growth_shovel_light.svg">
    <img alt="Shovel Recipes Growth" src="growth_shovel_light.svg" width="49%">
  </picture>
</p>

# 🚀 Getting Started
To add and use any of the buckets listed below, simply run the following command in your terminal:
```powershell
scoop bucket add <bucket-name> <bucket-url>
```
For example, to add a specific bucket, find its URL from the list below and run:
```powershell
scoop bucket add my-awesome-bucket https://github.com/user/my-awesome-bucket
```
After adding the bucket, you can install any of its applications like this:
```powershell
scoop install my-awesome-bucket/<app-name>
```

# Third party buckets by popularity

{% if hidden_gems %}
## 💎 Hidden Gems
These buckets are actively maintained and feature a high percentage of **unique** applications not found in official repositories. Great for discovering niche tools!

{% for repo in hidden_gems %}
### [{{repo.full_name}}]({{repo.html_url}})
*   **Unique Recipes:** {{repo.unique_count}} ({{ "%.1f"|format(repo.uniqueness_ratio * 100) }}% unique)
*   **Total Recipes:** {{ repo.entries|length }}
{% endfor %}
{% endif %}

{% if trending %}
## 🔥 Trending
These active buckets are rapidly climbing the ranks due to recent, high-quality updates and growing recipe counts!

{% for repo in trending %}
### [{{repo.full_name}}]({{repo.html_url}})
*   **Rank Change:** 📈 Up {{repo.rank_velocity}} spots! (Now Rank #{{repo.current_rank}})
*   **Total Recipes:** {{ repo.entries|length }}
{% endfor %}
{% endif %}

## 🥄 Scoop Compatible Buckets
These buckets are fully compatible with Scoop (and Shovel). They contain standard JSON manifests.

<details>
<summary><b>Click to expand {{ scoop_repos|length }} Scoop buckets</b></summary>

| Repository | Recipes | Score | Auto-Update | Badges |
| :--- | :---: | :---: | :---: | :--- |
{% for repo in scoop_repos %}
| **[{{repo.full_name}}](directory/{{repo.full_name|replace('/', '+')}}.md)** | 📦 {{ repo.entries|length }} | ⭐ {{repo.score}} | 🔄 {{ "%.0f"|format((repo.checkver_count / repo.entries|length * 100) if repo.entries|length > 0 else 0) }}% | {% if repo.is_scoop_official %}👑 Official Scoop{% elif repo.is_scoop_known %}⭐ Known Scoop{% endif %}{% if repo.is_shovel_official %}<br>👑 Official Shovel{% elif repo.is_shovel_known %}<br>⭐ Known Shovel{% endif %} |
{% endfor %}

</details>

## ⛏️ Shovel Specific Buckets
These buckets utilize Shovel-specific features (like native YAML manifests) or are explicitly tagged for Shovel. They may not work with standard Scoop.

<details>
<summary><b>Click to expand {{ shovel_repos|length }} Shovel buckets</b></summary>

| Repository | Recipes | Score | Auto-Update | Badges |
| :--- | :---: | :---: | :---: | :--- |
{% for repo in shovel_repos %}
| **[{{repo.full_name}}](directory/{{repo.full_name|replace('/', '+')}}.md)** | 📦 {{ repo.entries|length }} | ⭐ {{repo.score}} | 🔄 {{ "%.0f"|format((repo.checkver_count / repo.entries|length * 100) if repo.entries|length > 0 else 0) }}% | {% if repo.is_scoop_official %}👑 Official Scoop{% elif repo.is_scoop_known %}⭐ Known Scoop{% endif %}{% if repo.is_shovel_official %}<br>👑 Official Shovel{% elif repo.is_shovel_known %}<br>⭐ Known Shovel{% endif %} |
{% endfor %}

</details>

## 📦 All Known Buckets
A combined list of every bucket discovered in the ecosystem.

<details>
<summary><b>Click to expand all {{ all_repos|length }} discovered buckets</b></summary>

| Repository | Recipes | Score | Auto-Update | Badges |
| :--- | :---: | :---: | :---: | :--- |
{% for repo in all_repos %}
| **[{{repo.full_name}}](directory/{{repo.full_name|replace('/', '+')}}.md)** | 📦 {{ repo.entries|length }} | ⭐ {{repo.score}} | 🔄 {{ "%.0f"|format((repo.checkver_count / repo.entries|length * 100) if repo.entries|length > 0 else 0) }}% | {% if repo.is_scoop_official %}👑 Official Scoop{% elif repo.is_scoop_known %}⭐ Known Scoop{% endif %}{% if repo.is_shovel_official %}<br>👑 Official Shovel{% elif repo.is_shovel_known %}<br>⭐ Known Shovel{% endif %} |
{% endfor %}

</details>

# 🛠️ Operational Health (Crawler Metrics)
* **Total Crawler Runs**: {{ metrics.total_runs }}
* **Total Repo Updates**: {{ metrics.total_repo_updates }}
* **Ecosystem Growth (Since Last Run)**:
  * 🪣 {{ "%+d"|format(metrics.bucket_velocity) }} Buckets
  * 📦 {{ "%+d"|format(metrics.recipe_velocity) }} Recipes
* **Eviction Count**: 🗑️ {{ metrics.total_evictions }}
* **API Rate Limit Retries**: ⏳ {{ metrics.total_api_retries }}
* **Cache Size**: 💾 {{ "%.2f"|format(metrics.cache_size_mb) }} MB
* **Pipeline Times (Last Run)**:
  * 🔍 Discovery: {{ "%.2f"|format(metrics.last_run_discover_time) }}s
  * 📥 Update: {{ "%.2f"|format(metrics.last_run_update_time) }}s
* **Cumulative Compute Time**: {{ "%.1f"|format(metrics.total_run_time_seconds / 60) }} minutes
