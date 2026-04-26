from maintenance.config import get_config
MOCK_CONFIG = get_config('scoop_shovel')

import json

from maintenance.output import (
    generate_apis,
    generate_growth_charts,
    generate_readme,
    write_api_file,
)


def test_generate_growth_charts(tmp_path):
    timeseries = [
        {
            "date": "2026-04-25",
            "all": {"added": 10, "deleted": -2, "retained": 100},
            "scoop": {"added": 5, "deleted": -1, "retained": 50},
            "shovel": {"added": 5, "deleted": -1, "retained": 50},
        }
    ]
    dummy_dir = tmp_path / "dummy"
    dummy_dir.mkdir()
    generate_growth_charts(timeseries, str(dummy_dir))

    assert (dummy_dir / "growth_all_light.svg").exists()
    assert (dummy_dir / "growth_scoop_light.svg").exists()
    assert (dummy_dir / "growth_shovel_light.svg").exists()
    assert (dummy_dir / "growth_all_dark.svg").exists()
    assert (dummy_dir / "growth_scoop_dark.svg").exists()
    assert (dummy_dir / "growth_shovel_dark.svg").exists()


def test_generate_readme(tmp_path):
    actual_repos = [{"full_name": "user/repo", "score": 100}]
    scoop_repos = []
    shovel_repos = []
    hidden_gems = []
    trending = []
    metrics = {
        "total_runs": 1,
        "total_run_time_seconds": 120.5,
        "total_repo_updates": 5,
        "bucket_velocity": +2,
        "recipe_velocity": -5,
        "total_unique_recipes": 100,
        "auto_update_percentage": 50.0,
        "ecosystem_reliability": 98.5,
        "official_recipes": 50,
        "community_recipes": 50,
        "scoop_buckets": 1,
        "shovel_buckets": 1,
        "stale_buckets": 0,
        "total_evictions": 0,
        "total_api_retries": 0,
        "cache_size_mb": 1.5,
        "last_run_discover_time": 1.0,
        "last_run_update_time": 10.0,
    }

    # We need a dummy template directory to avoid Jinja2 errors
    template_dir = tmp_path / "template"
    template_dir.mkdir()
    template_file = template_dir / "ReadmeTemplate.tpl"
    template_file.write_text(
        "Test template with {{ all_repos[0].full_name }} and {{ metrics.total_runs }} runs"
    )
    bucket_template_file = template_dir / "BucketTemplate.tpl"
    bucket_template_file.write_text("Test bucket template")

    generate_readme(
        actual_repos,
        scoop_repos,
        shovel_repos,
        hidden_gems,
        trending,
        metrics,
        str(tmp_path),
        str(tmp_path),
    )

    readme_file = tmp_path / "README.md"
    assert readme_file.exists()
    content = readme_file.read_text()
    assert "Test template with user/repo" in content
    assert "and 1 runs" in content


def test_write_api_file(tmp_path):
    data = [{"name": "test"}]
    metrics = {"total_runs": 1}
    # write_api_file writes to `os.path.join(dir_path, "..", filename)`
    # Let's pass tmp_path / "dummy" so it writes to tmp_path
    dummy_dir = tmp_path / "dummy"
    dummy_dir.mkdir()

    write_api_file("test.json", "my_key", data, metrics, str(dummy_dir))

    output_file = dummy_dir / "test.json"
    assert output_file.exists()
    content = json.loads(output_file.read_text())
    assert content["my_key"] == data
    assert "metadata" in content
    assert content["metadata"]["count"] == 1
    assert content["metadata"]["global_metrics"] == metrics


def test_generate_apis(tmp_path, mocker):
    mock_write = mocker.patch("maintenance.output.write_api_file")
    metrics = {"total_runs": 1}
    generate_apis([], [], [], [], [], [], metrics, str(tmp_path))

    assert mock_write.call_count == 6
    mock_write.assert_any_call("all.json", "all", [], metrics, str(tmp_path))
