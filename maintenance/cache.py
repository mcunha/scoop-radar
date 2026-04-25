"""Functions related to cache management."""

import os
import pickle


def load_cache(dir_path):
    """Load the cache from disk."""
    try:
        with open(os.path.join(dir_path, "cache.pickle"), "rb") as input_file:
            return pickle.load(input_file)
    except (OSError, EOFError):
        return {}


def save_cache(cache, dir_path):
    """Save the cache to disk."""
    try:
        with open(os.path.join(dir_path, "cache.pickle"), "wb") as input_file:
            pickle.dump(cache, input_file)
    except OSError:
        pass


def upgrade_cache_entry(repofoldername, entry):
    """Ensure a cache entry has all required default fields."""
    if "full_name" not in entry:
        entry["full_name"] = repofoldername.replace("+", "/")
    if "git_url" not in entry or entry["git_url"].startswith("git://"):
        entry["git_url"] = f"https://github.com/{entry['full_name']}.git"
    if "html_url" not in entry:
        entry["html_url"] = entry.get("url", f"https://github.com/{entry['full_name']}")
    if "default_branch" not in entry:
        entry["default_branch"] = "master"
    if "topics" not in entry:
        entry["topics"] = []
    if "last_checked" not in entry:
        entry["last_checked"] = "2000-01-01T00:00:00Z"
    if "pushed_at" not in entry:
        entry["pushed_at"] = "2000-01-01T00:00:00Z"
    if "archived" not in entry:
        entry["archived"] = False
    if "disabled" not in entry:
        entry["disabled"] = False
    if "checkver_count" not in entry:
        entry["checkver_count"] = 0
    if "consecutive_failures" not in entry:
        entry["consecutive_failures"] = 0
    return entry
