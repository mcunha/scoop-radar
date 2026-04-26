# Awesome Package Managers Radar

A data-driven, automated discovery and ranking engine for Windows package manager ecosystems.

This repository tracks, ranks, and analyzes community repositories (buckets/feeds) to help users discover hidden gems, trending packages, and reliable sources.

## Supported Ecosystems

*   [**Scoop & Shovel**](./scoop_shovel/README.md): Tracking 📦 **86,228** Packages across 🪣 **221** Repositories
*   [**Chocolatey**](./chocolatey/README.md): Tracking 📦 **2,187** Packages across 🪣 **41** Sources
*   [**WinGet**](./winget/README.md): Tracking 📦 **5,411** Packages across 🪣 **5** Repositories

## How it works

The engine runs on GitHub Actions and performs the following tasks:
1.  **Discovery**: Scans GitHub for specific topics (e.g. `scoop-bucket`, `chocolatey-packages`) to find new repositories.
2.  **Validation**: Clones repositories and validates their manifests against official schemas.
3.  **Metrics**: Analyzes repository health based on update frequency, uniqueness, active maintenance, and staleness.
4.  **Generation**: Produces detailed markdown directories, SVG charts, and JSON APIs for the community to consume.

See [CONTRIBUTING.md](CONTRIBUTING.md) if you'd like to help improve the crawler.
