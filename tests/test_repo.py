from datetime import datetime, timezone

import maintenance.state as state
from maintenance.config import get_config
from maintenance.repo import get_next_check_due, is_manifest, process_repo, validate_manifest_file

MOCK_CONFIG = get_config("scoop_shovel")


def test_is_manifest():
    assert is_manifest("app.json") is True
    assert is_manifest("app.yaml") is True
    assert is_manifest("app.yml") is True
    assert is_manifest("app.txt") is False


def test_get_next_check_due():
    # First time check
    entry = {"last_checked": "2000-01-01T00:00:00Z"}
    assert get_next_check_due(entry) == datetime(2000, 1, 1, tzinfo=timezone.utc)

    # Ignored until
    entry = {"last_checked": "2023-01-01T00:00:00Z", "ignored_until": "2025-01-01T00:00:00Z"}
    assert get_next_check_due(entry) == datetime(2025, 1, 1, tzinfo=timezone.utc)

    # Archived
    entry = {"last_checked": "2023-01-01T00:00:00Z", "archived": True}
    assert get_next_check_due(entry).year == 2023
    assert get_next_check_due(entry).month == 1
    assert get_next_check_due(entry).day == 31


def test_validate_manifest_file_no_schema(tmp_path):
    state.SCHEMAS.pop("scoop", None)
    state.SCHEMAS.pop("shovel", None)

    file_path = tmp_path / "app.json"
    file_path.write_text('{"version": "1.0", "checkver": "regex"}')

    is_valid, has_checkver = validate_manifest_file(str(file_path), "app.json", False, MOCK_CONFIG)
    assert is_valid is True
    assert has_checkver is True


def test_validate_manifest_file_invalid_no_version(tmp_path):
    state.SCHEMAS.pop("scoop", None)
    state.SCHEMAS.pop("shovel", None)

    file_path = tmp_path / "app.json"
    file_path.write_text('{"description": "no version"}')

    is_valid, has_checkver = validate_manifest_file(str(file_path), "app.json", False, MOCK_CONFIG)
    assert is_valid is False
    assert has_checkver is False


def test_process_repo_ignored(mocker):
    # If ignored_until is in the future, it should just return and update last_checked
    entry = {"full_name": "user/repo", "ignored_until": "2099-01-01T00:00:00Z"}

    name, updated_entry, updated = process_repo("user+repo", entry, "/tmp", MOCK_CONFIG)
    assert updated is False
    assert "last_checked" in updated_entry
    assert updated_entry["ignored_until"] == "2099-01-01T00:00:00Z"
