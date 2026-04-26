# {{ ecosystem_name|replace('_', ' ')|title }} Radar
A data-driven, automated discovery and ranking engine for the {{ ecosystem_name|replace('_', ' ')|title }} package manager ecosystem on Windows

# Build Status
![Tests & Linting](https://github.com/mcunha/scoop-radar/actions/workflows/test.yml/badge.svg)
![Update Package Managers Radar](https://github.com/mcunha/scoop-radar/actions/workflows/update.yml/badge.svg)

# 📊 Ecosystem Health
* **Total Unique Recipes**: {{ metrics.total_unique_recipes }}
* **Ecosystem Auto-Update Health**: {{ metrics.auto_update_percentage }}%
* **Ecosystem Reliability**: {{ metrics.ecosystem_reliability }}% (Sampled URL Health)
* **Official vs. Community**: {{ metrics.official_recipes }} Official / {{ metrics.community_recipes }} Community
{% if ecosystem_name == 'scoop_shovel' %}* **Bucket Ecosystem**: {{ metrics.scoop_buckets }} Scoop / {{ metrics.shovel_buckets }} Shovel{% endif %}
* **Stale/Abandoned Sources (> 1 Year)**: 🪦 {{ metrics.stale_buckets }}

### Ecosystem Growth (All Recipes)
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="growth_all_dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="growth_all_light.svg">
  <img alt="All Recipes Growth" src="growth_all_light.svg">
</picture>

{% if ecosystem_name == 'scoop_shovel' %}
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
{% endif %}

# 🚀 Getting Started
To add and use any of the repositories listed below, run the appropriate command for your package manager:

{% if ecosystem_name == 'scoop_shovel' %}
```powershell
scoop bucket add <bucket-name> <bucket-url>
scoop install <bucket-name>/<app-name>
```
{% elif ecosystem_name == 'chocolatey' %}
```powershell
choco source add -n <source-name> -s <source-url>
choco install <app-name> --source <source-name>
```
{% elif ecosystem_name == 'winget' %}
```powershell
winget source add -n <source-name> -a <source-url>
winget install <app-name> --source <source-name>
```
{% endif %}

# Third party repositories by popularity

{% if hidden_gems %}
## 💎 Hidden Gems
These repositories are actively maintained and feature a high percentage of **unique** applications not found in official repositories. Great for discovering niche tools!

| Repository | Unique Recipes | Total Recipes | Score | Auto-Update |
| :--- | :---: | :---: | :---: | :---: |
{% for repo in hidden_gems -%}
| **[{{repo.full_name}}](directory/{{repo.full_name|replace('/', '+')}}.md)** | 💎 {{repo.unique_count}} ({{ "%.1f"|format(repo.uniqueness_ratio * 100) }}%) | 📦 {{ repo.entries|length }} | ⭐ {{repo.score}} | 🔄 {{ "%.0f"|format((repo.checkver_count / repo.entries|length * 100) if repo.entries|length > 0 else 0) }}% |
{% endfor %}
{% endif %}

{% if trending %}
## 🔥 Trending
These active repositories are rapidly climbing the ranks due to recent, high-quality updates and growing recipe counts!

| Repository | Rank Change | Current Rank | Recipes | Score | Auto-Update |
| :--- | :---: | :---: | :---: | :---: | :---: |
{% for repo in trending -%}
| **[{{repo.full_name}}](directory/{{repo.full_name|replace('/', '+')}}.md)** | 📈 +{{repo.rank_velocity}} | 🏆 #{{repo.current_rank}} | 📦 {{ repo.entries|length }} | ⭐ {{repo.score}} | 🔄 {{ "%.0f"|format((repo.checkver_count / repo.entries|length * 100) if repo.entries|length > 0 else 0) }}% |
{% endfor %}
{% endif %}

{% macro render_bucket_table(repos) -%}
| Repository | Recipes | Score | Auto-Update | Badges |
| :--- | :---: | :---: | :---: | :--- |
{% for repo in repos -%}
| **[{{repo.full_name}}](directory/{{repo.full_name|replace('/', '+')}}.md)** | 📦 {{ repo.entries|length }} | ⭐ {{repo.score}} | 🔄 {{ "%.0f"|format((repo.checkver_count / repo.entries|length * 100) if repo.entries|length > 0 else 0) }}% | {% if ecosystem_name == 'scoop_shovel' %}{% if repo.is_scoop_official %}👑 Official Scoop{% elif repo.is_scoop_known %}⭐ Known Scoop{% endif %}{% if repo.is_shovel_official %}<br>👑 Official Shovel{% elif repo.is_shovel_known %}<br>⭐ Known Shovel{% endif %}{% else %}{% if repo.is_scoop_official %}👑 Official{% endif %}{% endif %} |
{% endfor %}
{%- endmacro %}

{% if ecosystem_name == 'scoop_shovel' %}
## 🥄 Scoop Compatible Buckets
These buckets are fully compatible with Scoop (and Shovel). They contain standard JSON manifests.

<details>
<summary><b>Click to expand {{ scoop_repos|length }} Scoop buckets</b></summary>

{{ render_bucket_table(scoop_repos) }}
</details>

## ⛏️ Shovel Specific Buckets
These buckets utilize Shovel-specific features (like native YAML manifests) or are explicitly tagged for Shovel. They may not work with standard Scoop.

<details>
<summary><b>Click to expand {{ shovel_repos|length }} Shovel buckets</b></summary>

{{ render_bucket_table(shovel_repos) }}
</details>

{% endif %}

## 📦 All Known Sources
A combined list of every source discovered in the ecosystem.

<details>
<summary><b>Click to expand all {{ all_repos|length }} discovered sources</b></summary>

{{ render_bucket_table(all_repos) }}
</details>

# 🛠️ Operational Health (Crawler Metrics)
* **Total Crawler Runs**: {{ metrics.total_runs }}
* **Total Repo Updates**: {{ metrics.total_repo_updates }}
* **Ecosystem Growth (Since Last Run)**:
  * 🪣 {{ "%+d"|format(metrics.bucket_velocity) }} Repositories
  * 📦 {{ "%+d"|format(metrics.recipe_velocity) }} Recipes
* **Eviction Count**: 🗑️ {{ metrics.total_evictions }}
* **API Rate Limit Retries**: ⏳ {{ metrics.total_api_retries }}
* **Cache Size**: 💾 {{ "%.2f"|format(metrics.cache_size_mb) }} MB
* **Pipeline Times (Last Run)**:
  * 🔍 Discovery: {{ "%.2f"|format(metrics.last_run_discover_time) }}s
  * 📥 Update: {{ "%.2f"|format(metrics.last_run_update_time) }}s
* **Cumulative Compute Time**: {{ "%.1f"|format(metrics.total_run_time_seconds / 60) }} minutes
