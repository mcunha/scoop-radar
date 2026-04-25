"""Functions for generating the final output."""

import json
import os
from datetime import datetime, timezone

import pygal
from jinja2 import Environment, FileSystemLoader
from pygal.style import CleanStyle, Style

GitHubDarkStyle = Style(
    background="transparent",
    plot_background="transparent",
    foreground="#f0f6fc",
    foreground_strong="#f0f6fc",
    foreground_subtle="#9198a1",
    opacity=".6",
    opacity_hover=".9",
    transition="400ms ease-in",
    colors=("#58a6ff", "#3fb950", "#f85149", "#d29922", "#a371f7"),
)


def generate_growth_charts(timeseries, out_dir):
    """Generate SVG charts visualizing ecosystem growth and churn."""
    for ecosystem in ["all", "scoop", "shovel"]:
        # We only want to show the last 30 data points so it doesn't get too squished
        display_series = timeseries[-30:] if len(timeseries) > 30 else timeseries

        for theme_name, theme_style in [("light", CleanStyle), ("dark", GitHubDarkStyle)]:
            chart = pygal.StackedBar(
                style=theme_style,
                legend_at_bottom=True,
                show_y_guides=True,
                title=f"Recipe Churn: {ecosystem.capitalize()}",
                x_label_rotation=45,
                show_minor_y_labels=False,
            )

            # Don't show every single date label if we have lots of dates
            chart.x_labels = [t["date"] for t in display_series]

            retained = [t[ecosystem]["retained"] for t in display_series]
            added = [t[ecosystem]["added"] for t in display_series]
            deleted = [t[ecosystem]["deleted"] for t in display_series]  # these are negative

            chart.add("Retained", retained, color="#3498DB")
            chart.add("Added (Net New)", added, color="#2ECC71")
            chart.add("Deleted", deleted, color="#E74C3C")

            svg_path = os.path.join(out_dir, f"growth_{ecosystem}_{theme_name}.svg")
            chart.render_to_file(svg_path)
            with open(svg_path, "a", encoding="utf-8") as f:
                f.write("\n")


def generate_readme(
    actual_repos, scoop_repos, shovel_repos, hidden_gems, trending, metrics, out_dir, dir_path
):
    """Generate the main README.md file."""
    print(
        f"[*] {len(actual_repos)} total valid repositories ({len(scoop_repos)} Scoop, {len(shovel_repos)} Shovel)."
    )

    TEMPLATE_ENVIRONMENT = Environment(
        autoescape=False,
        loader=FileSystemLoader(os.path.join(dir_path, "template")),
        trim_blocks=False,
        keep_trailing_newline=True,
    )

    # Generate individual bucket markdown files
    buckets_dir = os.path.join(out_dir, "directory")
    os.makedirs(buckets_dir, exist_ok=True)
    bucket_template = TEMPLATE_ENVIRONMENT.get_template("BucketTemplate.tpl")

    for repo in actual_repos:
        safe_name = repo["full_name"].replace("/", "+") + ".md"
        bucket_content = bucket_template.render({"repo": repo})
        with open(os.path.join(buckets_dir, safe_name), "w", encoding="utf-8") as f:
            f.write(bucket_content)

    context = {
        "all_repos": actual_repos,
        "scoop_repos": scoop_repos,
        "shovel_repos": shovel_repos,
        "hidden_gems": hidden_gems,
        "trending": trending,
        "metrics": metrics,
    }

    markdown_content = TEMPLATE_ENVIRONMENT.get_template("ReadmeTemplate.tpl").render(context)
    with open(os.path.join(out_dir, "README.md"), "w", encoding="utf-8") as readme_file:
        readme_file.write(markdown_content)


def write_api_file(filename, data_key, data_list, metrics, out_dir):
    """Write an API JSON file to disk."""
    api_data = {
        data_key: data_list,
        "metadata": {
            "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "count": len(data_list),
            "global_metrics": metrics,
        },
    }
    with open(os.path.join(out_dir, filename), "w", encoding="utf-8") as json_file:
        json.dump(api_data, json_file, indent=2, ensure_ascii=False)
        json_file.write("\n")


def generate_apis(
    actual_repos, scoop_repos, shovel_repos, hidden_gems, trending, evictions, metrics, out_dir
):
    """Generate JSON API files for ecosystem consumption."""
    print(
        "[*] Generating Ecosystem APIs (all.json, scoop.json, shovel.json, trending.json, hidden_gems.json, evictions.json)..."
    )
    write_api_file("all.json", "all", actual_repos, metrics, out_dir)
    write_api_file("scoop.json", "scoop", scoop_repos, metrics, out_dir)
    write_api_file("shovel.json", "shovel", shovel_repos, metrics, out_dir)
    write_api_file("hidden_gems.json", "hidden_gems", hidden_gems, metrics, out_dir)
    write_api_file("trending.json", "trending", trending, metrics, out_dir)
    write_api_file("evictions.json", "evictions", evictions, metrics, out_dir)
