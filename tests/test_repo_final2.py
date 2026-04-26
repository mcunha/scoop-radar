from maintenance.config import get_config
MOCK_CONFIG = get_config('scoop_shovel')

from maintenance.repo import process_repo, update_repositories



def test_process_repo_new_clone_exception(mocker):
    # Covers line 167
    cache_entry = {
        "last_checked": "2000-01-01T00:00:00Z",
        "topics": ["scoop-bucket"],
        "default_branch": "main",
        "full_name": "user/repo",
    }
    mocker.patch("maintenance.repo.Repo.clone_from", side_effect=Exception("Failed to clone"))
    mocker.patch("os.path.isdir", return_value=False)
    name, updated_entry, updated = process_repo("user+repo", cache_entry, "/tmp", MOCK_CONFIG)
    assert updated is True


def test_process_repo_existing_clone_exception(mocker):
    # Covers line 193
    cache_entry = {"last_checked": "2023-01-01T00:00:00Z", "topics": ["scoop-bucket"]}
    mocker.patch("os.path.isdir", side_effect=[False, False])
    mocker.patch(
        "maintenance.repo.Repo.clone_from", side_effect=Exception("Failed to clone existing")
    )
    name, updated_entry, updated = process_repo("user+repo", cache_entry, "/tmp", MOCK_CONFIG)
    assert updated is True


def test_process_repo_new_not_bucket_manifest_in_tree(mocker):
    # Covers lines 132, 135-136, 138-152
    cache_entry = {
        "last_checked": "2000-01-01T00:00:00Z",
        "topics": [],
        "default_branch": "main",
        "full_name": "user/repo",
    }

    mock_make_request = mocker.patch("maintenance.repo.make_request")
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"tree": [{"path": "app.json", "type": "blob"}]}
    mock_make_request.return_value = mock_response

    mocker.patch("maintenance.repo.Repo")
    mocker.patch("os.path.isdir", return_value=False)

    name, updated_entry, updated = process_repo("user+repo", cache_entry, "/tmp", MOCK_CONFIG)
    assert updated is True


def test_update_repositories_with_results(mocker):
    # Covers 235-241
    cache = {"user+repo": {"last_checked": "2000-01-01T00:00:00Z"}}
    mocker.patch(
        "maintenance.repo.process_repo", return_value=("user+repo", {"updated": True}, True)
    )
    update_repositories(cache, "/tmp", MOCK_CONFIG)
    assert cache["user+repo"]["updated"] is True
