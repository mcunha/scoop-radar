# {{ repo.full_name }}

* **Repository:** [{{ repo.html_url }}]({{ repo.html_url }})
* **Score:** {{ repo.score }}
* **Auto-Update:** {{ "%.0f"|format((repo.checkver_count / repo.entries|length * 100) if repo.entries|length > 0 else 0) }}%
{% if repo.is_scoop_official %}* **Status:** 👑 Official Scoop Bucket{% elif repo.is_scoop_known %}* **Status:** ⭐ Known Scoop Bucket{% endif %}
{% if repo.is_shovel_official %}* **Status:** 👑 Official Shovel Bucket{% elif repo.is_shovel_known %}* **Status:** ⭐ Known Shovel Bucket{% endif %}

## 📦 Recipes ({{ repo.entries|length }})
{% for entry in repo.entries -%}
  * [{{ entry }}]({{ repo.html_url }}/blob/{{ repo.default_branch }}/{{ entry }})
{% endfor -%}
