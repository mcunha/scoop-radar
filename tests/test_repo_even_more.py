from maintenance.config import get_config
MOCK_CONFIG = get_config('scoop_shovel')

from datetime import datetime, timezone

from maintenance.repo import get_next_check_due, process_repo



def test_get_next_check_due_disabled():
    entry = {"last_checked": "2023-01-01T00:00:00Z", "disabled": True}
    due = get_next_check_due(entry)
    assert due == datetime(2023, 1, 31, tzinfo=timezone.utc)


def test_get_next_check_due_recent_push():
    # If pushed recently, interval should be smaller
    now = datetime.now(timezone.utc)
    pushed = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    entry = {"last_checked": "2023-01-01T00:00:00Z", "pushed_at": pushed}
    due = get_next_check_due(entry)
    # the interval will be the minimum, which is 6 hours
    assert due == datetime(2023, 1, 1, 6, 0, tzinfo=timezone.utc)


def test_process_repo_new_not_bucket(mocker):
    cache_entry = {
        "last_checked": "2000-01-01T00:00:00Z",
        "topics": [],
        "default_branch": "main",
        "full_name": "user/repo",
    }

    mock_make_request = mocker.patch("maintenance.repo.make_request")
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"tree": [{"path": "readme.md", "type": "blob"}]}
    mock_make_request.return_value = mock_response

    name, updated_entry, updated = process_repo("user+repo", cache_entry, "/tmp", MOCK_CONFIG)
    assert updated is True
    assert updated_entry["checkver_count"] == 0
    assert "ignored_until" in updated_entry


def test_process_repo_existing_clone_error(mocker):
    cache_entry = {"last_checked": "2023-01-01T00:00:00Z"}

    mocker.patch("os.path.isdir", return_value=False)

    mock_repo = mocker.patch("maintenance.repo.Repo")
    mock_repo.clone_from.side_effect = Exception("Clone failed")

    name, updated_entry, updated = process_repo("user+repo", cache_entry, "/tmp", MOCK_CONFIG)
    assert updated is True
    assert updated_entry["checkver_count"] == 0


def test_process_repo_existing_pull(mocker):
    cache_entry = {"last_checked": "2023-01-01T00:00:00Z"}

    # First os.path.isdir for the git repo check, then for the bucket directories
    mocker.patch("os.path.isdir", side_effect=[True, False, False])

    mock_repo = mocker.patch("maintenance.repo.Repo")

    name, updated_entry, updated = process_repo("user+repo", cache_entry, "/tmp", MOCK_CONFIG)
    assert updated is True
    assert mock_repo.call_count == 1


def test_process_repo_existing_pull_error(mocker):
    cache_entry = {"last_checked": "2023-01-01T00:00:00Z"}

    mocker.patch("os.path.isdir", side_effect=[True, False, False])

    mock_repo = mocker.patch("maintenance.repo.Repo")
    mock_repo.return_value.remotes.origin.pull.side_effect = Exception("Pull failed")

    name, updated_entry, updated = process_repo("user+repo", cache_entry, "/tmp", MOCK_CONFIG)
    assert updated is True
