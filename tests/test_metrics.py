from maintenance.config import get_config
MOCK_CONFIG = get_config('scoop_shovel')

from datetime import datetime, timezone

from hypothesis import given
from hypothesis import strategies as st

from maintenance.metrics import get_repo_score


@given(
    score=st.floats(min_value=0.0, max_value=100.0, allow_nan=False, allow_infinity=False),
    entries_count=st.integers(min_value=0, max_value=10000),
    days_since_push=st.integers(min_value=0, max_value=3650),
)
def test_get_repo_score_properties(score, entries_count, days_since_push):
    """Property-based test for repository scoring logic."""
    pushed_at = datetime.now(timezone.utc).timestamp() - (days_since_push * 24 * 3600)
    pushed_at_str = datetime.fromtimestamp(pushed_at, tz=timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )

    # Generate mock entries
    entries = [f"app{i}.json" for i in range(entries_count)]

    repo = {"score": score, "entries": entries, "pushed_at": pushed_at_str}
    official_recipes = set()

    final_score = get_repo_score(repo, official_recipes)

    # Score should always be a float and shouldn't crash
    assert isinstance(final_score, float)

    # Check bounds
    # Staleness penalty can make score negative if unmaintained for a very long time
    if days_since_push > 180 and entries_count > 0:
        assert final_score < 25000.0  # reasonable upper bound
    else:
        assert final_score >= -200.0  # Allow some slack for extreme penalties


def test_get_repo_score_benchmark(benchmark):
    """Benchmark test for the scoring logic."""
    repo = {
        "score": 50.0,
        "entries": ["app1.json", "app2.json", "app3.json"],
        "pushed_at": "2023-01-01T00:00:00Z",
    }
    official_recipes = {"app1.json"}

    # Run the benchmark
    result = benchmark(get_repo_score, repo, official_recipes)

    assert isinstance(result, float)
