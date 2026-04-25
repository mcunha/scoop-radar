"""Functions for GitHub API interactions."""

import os
import time

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

import maintenance.state as state


class RateLimitExceededError(Exception):
    """Raised when the GitHub API rate limit is exceeded."""

    pass


session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retries))


def get_headers():
    """Get headers for GitHub API requests including authentication if available."""
    headers = {}
    if "GITHUB_TOKEN" in os.environ:
        headers["Authorization"] = f"token {os.environ['GITHUB_TOKEN']}"
    return headers


def make_request(url, headers):
    """Make an HTTP request with automatic retries for rate limits."""
    while True:
        if state.abort_flag:
            raise RateLimitExceededError("Aborted by another thread.")

        response = session.get(url, headers=headers)

        if response.status_code in [403, 429]:
            retry_after = response.headers.get("Retry-After")
            if retry_after:
                wait_time = int(retry_after)
            elif response.headers.get("X-RateLimit-Remaining") == "0":
                reset_time = int(response.headers.get("X-RateLimit-Reset", time.time() + 60))
                wait_time = reset_time - int(time.time()) + 1
            else:
                # Secondary rate limit or abuse detection without explicit headers
                wait_time = 60

            if wait_time > 0:
                if (
                    wait_time > 60
                ):  # Abort if wait is > 60 seconds to save CI minutes and avoid thread spam
                    print(
                        f"[!] Rate limit reached. Required wait time {wait_time}s is too long. Aborting gracefully."
                    )
                    state.abort_flag = True
                    raise RateLimitExceededError()

                print(
                    f"[!] Rate limited (Status {response.status_code}). Waiting {wait_time}s before retrying..."
                )
                state.api_retries += 1
                time.sleep(wait_time)
                continue

        return response


def fetchjson(urlstr):
    """Fetch and parse JSON from a URL."""
    response = make_request(urlstr, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    return {}


def fetch_schema_with_etag(url, cache_key, cache):
    """Fetch a JSON schema utilizing ETag caching."""
    headers = get_headers()
    cached_data = cache.get(cache_key, {})
    last_known_good = cached_data.get("schema")

    if "etag" in cached_data:
        headers["If-None-Match"] = cached_data["etag"]

    try:
        response = make_request(url, headers=headers)
        if response.status_code == 304:
            print(f"[*] Schema {cache_key} not modified (304). Using last known good.")
            return last_known_good
        elif response.status_code == 200:
            content = response.content
            if len(content) < 500 or len(content) > 5 * 1024 * 1024:
                print(
                    f"[!] Warning: Fetched schema {cache_key} failed size validation ({len(content)} bytes). Falling back to last known good."
                )
                return last_known_good

            schema = response.json()

            if not isinstance(schema, dict) or (
                "$schema" not in schema and "properties" not in schema
            ):
                print(
                    f"[!] Warning: Fetched schema {cache_key} failed structural validation. Falling back to last known good."
                )
                return last_known_good

            cache[cache_key] = {"etag": response.headers.get("ETag"), "schema": schema}
            print(f"[*] Schema {cache_key} fetched and validated successfully (200).")
            return schema
    except Exception as e:
        print(f"[!] Warning: Could not fetch schema {cache_key}. Error: {e}")

    return last_known_good
