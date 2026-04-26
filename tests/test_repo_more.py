import maintenance.state as state
from maintenance.config import get_config
from maintenance.repo import process_repo, validate_manifest_file

MOCK_CONFIG = get_config("scoop_shovel")


def test_validate_manifest_yaml(tmp_path):
    state.SCHEMAS.pop("scoop", None)
    state.SCHEMAS.pop("shovel", None)

    file_path = tmp_path / "app.yaml"
    file_path.write_text('version: "1.0"\ncheckver: "regex"')

    is_valid, has_checkver = validate_manifest_file(str(file_path), "app.yaml", False, MOCK_CONFIG)
    assert is_valid is True
    assert has_checkver is True


def test_validate_manifest_json_with_schema(tmp_path):
    state.SCHEMAS["scoop"] = {"type": "object", "properties": {"version": {"type": "string"}}}
    state.SCHEMAS.pop("shovel", None)

    file_path = tmp_path / "app.json"
    file_path.write_text('{"version": "1.0", "checkver": "regex"}')

    is_valid, has_checkver = validate_manifest_file(str(file_path), "app.json", False, MOCK_CONFIG)
    assert is_valid is True
    assert has_checkver is True


def test_process_repo_new_fetch_tree(mocker):
    cache_entry = {
        "last_checked": "2000-01-01T00:00:00Z",
        "topics": ["other"],
        "default_branch": "main",
        "full_name": "user/repo",
    }

    mock_make_request = mocker.patch("maintenance.repo.make_request")
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "tree": [{"path": "bucket", "type": "tree"}, {"path": "app.json", "type": "blob"}]
    }
    mock_make_request.return_value = mock_response

    mocker.patch("maintenance.repo.Repo")
    mocker.patch("os.path.isdir", side_effect=[True, True, False])
    mocker.patch("os.listdir", return_value=["app1.json"])
    mocker.patch("os.path.isfile", return_value=True)
    mocker.patch("maintenance.repo.validate_manifest_file", return_value=(True, True))

    name, updated_entry, updated = process_repo("user+repo", cache_entry, "/tmp", MOCK_CONFIG)
    assert updated is True
    assert mock_make_request.call_count == 1
