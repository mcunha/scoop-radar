import os

from maintenance.cache import load_cache, save_cache, upgrade_cache_entry
from maintenance.config import get_config

MOCK_CONFIG = get_config("scoop_shovel")


def test_load_cache_empty(tmp_path):
    """Test loading cache when file does not exist."""
    cache = load_cache(str(tmp_path))
    assert cache == {"CACHE_VERSION": 4}


def test_save_and_load_cache(tmp_path):
    """Test saving and loading cache data."""
    test_data = {"repo1": {"name": "test"}}
    save_cache(test_data, str(tmp_path))

    assert os.path.exists(os.path.join(str(tmp_path), "cache.pickle"))

    loaded_cache = load_cache(str(tmp_path))
    expected_data = {"repo1": {"name": "test"}, "CACHE_VERSION": 4}
    assert loaded_cache == expected_data


def test_upgrade_cache_entry_defaults():
    """Test upgrade_cache_entry sets missing default fields."""
    entry = {}
    upgraded = upgrade_cache_entry("user+repo", entry)

    assert upgraded["full_name"] == "user/repo"
    assert upgraded["git_url"] == "https://github.com/user/repo.git"
    assert upgraded["html_url"] == "https://github.com/user/repo"
    assert upgraded["default_branch"] == "master"
    assert upgraded["topics"] == []
    assert upgraded["last_checked"] == "2000-01-01T00:00:00Z"
    assert upgraded["pushed_at"] == "2000-01-01T00:00:00Z"
    assert upgraded["archived"] is False
    assert upgraded["disabled"] is False
    assert upgraded["checkver_count"] == 0


def test_upgrade_cache_entry_preserves_existing():
    """Test upgrade_cache_entry does not overwrite existing fields."""
    entry = {"full_name": "custom/repo", "default_branch": "main", "archived": True}
    upgraded = upgrade_cache_entry("user+repo", entry)

    assert upgraded["full_name"] == "custom/repo"
    assert upgraded["default_branch"] == "main"
    assert upgraded["archived"] is True
