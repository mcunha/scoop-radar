from datetime import datetime, timezone

import pytest

import maintenance.state as state
from maintenance.api import RateLimitExceededError
from maintenance.repo import (
    discover_repositories,
    get_next_check_due,
    process_repo,
    update_repositories,
    validate_manifest_file,
)


def test_get_next_check_due_no_pushed_at():
    # Covers line 41
    entry = {"last_checked": "2023-01-01T00:00:00Z"}
    due = get_next_check_due(entry)
    assert due > datetime(2023, 1, 1, tzinfo=timezone.utc)


def test_validate_manifest_file_exception(tmp_path):
    # Covers lines 76-77
    state.SCOOP_SCHEMA = None
    state.SHOVEL_SCHEMA = None
    file_path = tmp_path / "app.json"
    file_path.write_text("invalid json")
    is_valid, has_checkver = validate_manifest_file(str(file_path), "app.json", False)
    assert is_valid is False


def test_process_repo_abort_flag():
    # Covers line 85
    state.abort_flag = True
    assert process_repo("repo", {}, "/tmp") is None
    state.abort_flag = False


def test_process_repo_del_ignored_until(mocker):
    # Covers line 95
    cache_entry = {
        "last_checked": "2023-01-01T00:00:00Z",
        "ignored_until": "2000-01-01T00:00:00Z",
        "topics": ["scoop-bucket"],
    }
    mocker.patch("maintenance.repo.Repo")
    mocker.patch("os.path.isdir", return_value=False)
    name, updated_entry, updated = process_repo("user+repo", cache_entry, "/tmp")
    assert "ignored_until" not in updated_entry


def test_process_repo_not_official_tree_error(mocker):
    # Covers exception in tree fetch
    cache_entry = {
        "last_checked": "2000-01-01T00:00:00Z",
        "topics": [],
        "default_branch": "main",
        "full_name": "user/repo",
    }
    mock_make_request = mocker.patch(
        "maintenance.repo.make_request", side_effect=RateLimitExceededError
    )
    with pytest.raises(RateLimitExceededError):
        process_repo("user+repo", cache_entry, "/tmp")


def test_discover_repositories_rate_limit(mocker):
    # Covers lines 212-213
    mocker.patch("maintenance.repo.fetchjson", side_effect=RateLimitExceededError)
    cache = {"search_page": 1}
    discover_repositories(cache)
    assert state.abort_flag is False


def test_update_repositories_rate_limit(mocker):
    # Covers lines 277-284
    cache = {
        "user+repo1": {"last_checked": "2000-01-01T00:00:00Z"},
        "user+repo2": {"last_checked": "2000-01-01T00:00:00Z"},
    }

    def mock_process(*args, **kwargs):
        raise RateLimitExceededError()

    mocker.patch("maintenance.repo.process_repo", side_effect=mock_process)

    update_repositories(cache, "/tmp")

    assert state.abort_flag is True
