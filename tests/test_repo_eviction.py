from maintenance.config import get_config
from maintenance.repo import process_repo

MOCK_CONFIG = get_config("scoop_shovel")


def test_process_repo_eviction_404(mocker):
    # Ensure it triggers eviction
    cache_entry = {
        "last_checked": "2023-01-01T00:00:00Z",
        "consecutive_failures": 2,  # Will become 3 after failure
        "full_name": "user/repo",
        "git_url": "git://github.com/user/repo",
        "default_branch": "main",
        "topics": [],
    }

    mocker.patch("maintenance.repo.Repo")
    mocker.patch("os.path.isdir", return_value=False)
    mocker.patch("maintenance.repo.Repo.clone_from", side_effect=Exception("Failed"))

    # Mock GitHub API returning 404
    mock_make_request = mocker.patch("maintenance.repo.make_request")
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mock_make_request.return_value = mock_response

    mock_rmtree = mocker.patch("shutil.rmtree")
    mocker.patch("os.path.exists", return_value=True)  # mock repo_path exists for rmtree

    _name, entry, updated = process_repo("user+repo", cache_entry, "/tmp", MOCK_CONFIG)

    assert entry is None
    assert updated is True
    assert mock_make_request.call_count == 1
    assert mock_rmtree.call_count == 1


def test_process_repo_eviction_not_404(mocker):
    # Ensure it does NOT trigger eviction if API doesn't 404
    cache_entry = {
        "last_checked": "2023-01-01T00:00:00Z",
        "consecutive_failures": 2,
        "full_name": "user/repo",
        "git_url": "git://github.com/user/repo",
        "default_branch": "main",
        "topics": [],
    }

    mocker.patch("maintenance.repo.Repo")
    mocker.patch("os.path.isdir", return_value=False)
    mocker.patch("maintenance.repo.Repo.clone_from", side_effect=Exception("Failed"))

    # Mock GitHub API returning 200 (repo exists, just transient git error)
    mock_make_request = mocker.patch("maintenance.repo.make_request")
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_make_request.return_value = mock_response

    _name, entry, updated = process_repo("user+repo", cache_entry, "/tmp", MOCK_CONFIG)

    assert entry is not None
    assert entry["consecutive_failures"] == 3
    assert updated is True
