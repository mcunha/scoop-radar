from maintenance.cache import load_cache, save_cache, upgrade_cache_entry
from maintenance.config import get_config

MOCK_CONFIG = get_config("scoop_shovel")


def test_load_cache_oserror(mocker):
    mocker.patch("builtins.open", side_effect=OSError("Permission denied"))
    cache = load_cache("/tmp")
    assert cache == {"CACHE_VERSION": 4}


def test_save_cache_oserror(mocker):
    mocker.patch("builtins.open", side_effect=OSError("Permission denied"))
    save_cache({"test": "data"}, "/tmp")
    # Should silently pass


def test_upgrade_cache_entry_url_fallback():
    entry = {"url": "https://custom.com/user/repo"}
    # This will hit `entry.get("url", f"https://github.com/{entry['full_name']}")`
    upgraded = upgrade_cache_entry("user+repo", entry)
    assert upgraded["html_url"] == "https://custom.com/user/repo"
