from unittest.mock import patch

import responses

from maintenance.config import get_config
from maintenance.metrics import calculate_metrics, extract_github_repos

MOCK_CONFIG = get_config("scoop_shovel")


@responses.activate
def test_extract_github_repos():
    # Mock the API call inside extract_github_repos
    url = "https://api.github.com/repos"
    mock_data = {
        "repo1": "https://github.com/user/repo1.git",
        "repo2": "https://github.com/user/repo2",
        "not_a_repo": "some_other_string",
    }
    responses.add(responses.GET, url, json=mock_data, status=200)

    repos = extract_github_repos(url)
    assert "user/repo1" in repos
    assert "user/repo2" in repos
    assert len(repos) == 2


@patch("maintenance.metrics.extract_github_repos")
def test_calculate_metrics(mock_extract):
    mock_extract.side_effect = [
        ["user/official_scoop"],  # KNOWN_SCOOP_BUCKETS
        ["user/official_shovel"],  # KNOWN_SHOVEL_BUCKETS
    ]

    cache = {
        "user+repo1": {
            "full_name": "user/repo1",
            "score": 50,
            "entries": ["app1.json", "app2.yml"],
            "topics": ["shovel-bucket"],
            "pushed_at": "2023-01-01T00:00:00Z",
            "checkver_count": 1,
        },
        "user+repo2": {
            "full_name": "user/repo2",
            "score": 100,
            "entries": ["app3.json"],
            "topics": ["scoop-bucket"],
            "pushed_at": "2023-01-01T00:00:00Z",
            "checkver_count": 0,
        },
        "scoopinstaller+main": {
            "full_name": "scoopinstaller/main",
            "score": 100,
            "entries": ["app1.json"],
            "topics": [],
            "pushed_at": "2023-01-01T00:00:00Z",
        },
    }

    actual_repos, scoop_repos, shovel_repos, trending, hidden_gems, ecosystem_metrics = (
        calculate_metrics(cache, MOCK_CONFIG)
    )

    assert len(actual_repos) == 3

    # User repo1 has a .yml file and a shovel-bucket topic, so it should be in shovel_repos
    assert len(shovel_repos) == 1
    assert shovel_repos[0]["full_name"] == "user/repo1"

    # Others in scoop_repos
    assert len(scoop_repos) == 2

    # Metrics calculations checks
    for repo in actual_repos:
        assert "final_score" in repo
        assert "current_rank" in repo
        assert "rank_velocity" in repo
