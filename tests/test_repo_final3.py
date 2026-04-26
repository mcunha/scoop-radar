from datetime import datetime, timezone

from maintenance.config import get_config
from maintenance.repo import get_next_check_due

MOCK_CONFIG = get_config("scoop_shovel")


def test_get_next_check_due_empty_pushed_at():
    # Covers line 41 in repo.py
    entry = {"last_checked": "2023-01-01T00:00:00Z", "pushed_at": ""}
    due = get_next_check_due(entry)
    # The interval should be roughly from 2000-01-01 to 2023-01-01 / 10, which hits the max 30 days
    assert due == datetime(2023, 1, 31, tzinfo=timezone.utc)


def test_get_next_check_due_none_pushed_at():
    # Covers line 41 in repo.py
    entry = {"last_checked": "2023-01-01T00:00:00Z", "pushed_at": None}
    due = get_next_check_due(entry)
    assert due == datetime(2023, 1, 31, tzinfo=timezone.utc)
