from maintenance.config import get_config
MOCK_CONFIG = get_config('scoop_shovel')

from maintenance.metrics import calculate_metrics, get_repo_score



def test_get_repo_score_empty_pushed_at():
    repo = {
        "score": 10.0,
        "entries": ["app1.json"],
        "pushed_at": "",  # empty string should trigger `if not pushed_at_str:` branch
    }
    official_recipes = set()
    score = get_repo_score(repo, official_recipes)
    assert isinstance(score, float)


def test_calculate_metrics_missing_topics_and_entries():
    cache = {
        "user+repo": {
            "full_name": "user/repo",
            "score": 50.0,
            # Missing topics
            # Missing entries
            "pushed_at": "2023-01-01T00:00:00Z",
        }
    }
    # Doesn't have entries, so it will be filtered out of actual_repos
    actual_repos, scoop_repos, shovel_repos, trending, hidden_gems, ecosystem_metrics = (
        calculate_metrics(cache, MOCK_CONFIG)
    )
    assert len(actual_repos) == 0
