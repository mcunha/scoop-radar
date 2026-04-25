# awesome-scoop
A collection of awesome resource for the scoop package manager for windows

# Build Status
![Build Status](https://travis-ci.org/tapannallan/awesome-scoop.svg?branch=master)

# Third party buckets by popularity

## 🥄 Scoop Compatible Buckets
These buckets are fully compatible with Scoop (and Shovel). They contain standard JSON manifests.

{% for repo in scoop_repos %}
### [{{repo.full_name}}]({{repo.html_url}}) (Score: {{repo.score}})
{% for entry in repo.entries -%}
  * [{{ entry }}]({{ repo.html_url }}/blob/{{ repo.default_branch }}/{{ entry }})
{% endfor -%}

{% endfor %}

## ⛏️ Shovel Specific Buckets
These buckets utilize Shovel-specific features (like native YAML manifests) or are explicitly tagged for Shovel. They may not work with standard Scoop.

{% for repo in shovel_repos %}
### [{{repo.full_name}}]({{repo.html_url}}) (Score: {{repo.score}})
{% for entry in repo.entries -%}
  * [{{ entry }}]({{ repo.html_url }}/blob/{{ repo.default_branch }}/{{ entry }})
{% endfor -%}

{% endfor %}

## 📦 All Known Buckets
A combined list of every bucket discovered in the ecosystem.

{% for repo in all_repos %}
### [{{repo.full_name}}]({{repo.html_url}}) (Score: {{repo.score}})
{% for entry in repo.entries -%}
  * [{{ entry }}]({{ repo.html_url }}/blob/{{ repo.default_branch }}/{{ entry }})
{% endfor -%}

{% endfor %}