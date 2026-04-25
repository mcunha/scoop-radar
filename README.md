# scoop-radar
A collection of awesome resource for the scoop package manager for windows

# Build Status
![Tests & Linting](https://github.com/mcunha/scoop-radar/actions/workflows/test.yml/badge.svg)
![Update Scoop Radar README](https://github.com/mcunha/scoop-radar/actions/workflows/update.yml/badge.svg)

# Acknowledgements
This project was heavily inspired by the original `awesome-scoop` directories maintained by [algomaniac](https://github.com/algomaniac) and [tapannallan](https://github.com/tapannallan).

# 📊 Ecosystem Health
* **Total Unique Recipes**: 0
* **Ecosystem Auto-Update Health**: 0.0%
* **Ecosystem Reliability**: 100.0% (Sampled URL Health)
* **Official vs. Community**: 0 Official / 0 Community
* **Bucket Ecosystem**: 0 Scoop / 0 Shovel
* **Bucket Graveyard (Stale > 1 Year)**: 🪦 0

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





## 🥄 Scoop Compatible Buckets
These buckets are fully compatible with Scoop (and Shovel). They contain standard JSON manifests.



## ⛏️ Shovel Specific Buckets
These buckets utilize Shovel-specific features (like native YAML manifests) or are explicitly tagged for Shovel. They may not work with standard Scoop.



## 📦 All Known Buckets
A combined list of every bucket discovered in the ecosystem.



# 🛠️ Operational Health (Crawler Metrics)
* **Total Crawler Runs**: 2
* **Total Repo Updates**: 0
* **Ecosystem Growth (Since Last Run)**:
  * 🪣 +0 Buckets
  * 📦 +0 Recipes
* **Eviction Count**: 🗑️ 0
* **API Rate Limit Retries**: ⏳ 0
* **Cache Size**: 💾 0.02 MB
* **Pipeline Times (Last Run)**:
  * 🔍 Discovery: 0.21s
  * 📥 Update: 0.00s
* **Cumulative Compute Time**: 0.0 minutes
