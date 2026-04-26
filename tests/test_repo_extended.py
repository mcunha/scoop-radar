from maintenance.config import get_config
from maintenance.repo import discover_repositories, process_repo, update_repositories

MOCK_CONFIG = get_config("scoop_shovel")


def test_process_repo_new(mocker):
    cache_entry = {"last_checked": "2000-01-01T00:00:00Z", "topics": ["scoop-bucket"]}

    mocker.patch("maintenance.repo.Repo")
    mocker.patch(
        "os.path.isdir", side_effect=[True, True, False]
    )  # cache dir, repo_path, bucket path
    mocker.patch("os.listdir", return_value=["app1.json"])
    mocker.patch("os.path.isfile", return_value=True)
    mocker.patch("maintenance.repo.validate_manifest_file", return_value=(True, True))

    name, updated_entry, updated = process_repo("user+repo", cache_entry, "/tmp", MOCK_CONFIG)
    assert updated is True
    assert updated_entry["checkver_count"] == 1
    assert "app1.json" in updated_entry["entries"]


def test_process_repo_existing(mocker):
    cache_entry = {"last_checked": "2023-01-01T00:00:00Z"}

    mock_repo = mocker.patch("maintenance.repo.Repo")
    mocker.patch(
        "os.path.isdir", side_effect=[True, True, False, True, True, False]
    )  # Allow enough calls
    mocker.patch("os.listdir", return_value=["app2.json"])
    mocker.patch("os.path.isfile", return_value=True)
    mocker.patch("maintenance.repo.validate_manifest_file", return_value=(True, False))

    name, updated_entry, updated = process_repo("user+repo", cache_entry, "/tmp", MOCK_CONFIG)
    assert updated is True
    assert updated_entry["checkver_count"] == 0
    assert "bucket/app2.json" in updated_entry["entries"]


def test_discover_repositories(mocker):
    mock_fetchjson = mocker.patch("maintenance.repo.fetchjson")
    mock_fetchjson.return_value = {
        "items": [
            {
                "name": "repo1",
                "full_name": "user/repo1",
                "git_url": "git://github.com/user/repo1.git",
                "html_url": "https://github.com/user/repo1",
                "score": 100.0,
                "default_branch": "master",
                "topics": ["scoop-bucket"],
                "pushed_at": "2023-01-01T00:00:00Z",
                "archived": False,
                "disabled": False,
            }
        ]
    }

    cache = {"search_page": 1}
    discover_repositories(cache, MOCK_CONFIG)

    assert cache["search_page"] == 2
    assert "user+repo1" in cache
    assert cache["user+repo1"]["name"] == "repo1"


def test_update_repositories(mocker):
    mocker.patch(
        "maintenance.repo.process_repo", return_value=("user+repo", {"updated": True}, True)
    )

    cache = {"user+repo": {"last_checked": "2000-01-01T00:00:00Z"}}

    update_repositories(cache, "/tmp", MOCK_CONFIG)

    # Check if the process_repo mock was called
    assert cache["user+repo"]["updated"] is True
