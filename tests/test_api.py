import json
from unittest.mock import patch

import pytest
from maintenance.config import get_config
MOCK_CONFIG = get_config('scoop_shovel')

import responses

import maintenance.state as state
from maintenance.api import (
    RateLimitExceededError,
    fetch_schema_with_etag,
    fetchjson,
    get_headers,
    make_request,
)


def test_get_headers_no_token(monkeypatch):
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    headers = get_headers()
    assert "Authorization" not in headers


def test_get_headers_with_token(monkeypatch):
    monkeypatch.setenv("GITHUB_TOKEN", "test_token")
    headers = get_headers()
    assert headers["Authorization"] == "token test_token"


@responses.activate
def test_make_request_success():
    responses.add(responses.GET, "https://api.github.com/test", json={"status": "ok"}, status=200)
    resp = make_request("https://api.github.com/test", headers={})
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


@responses.activate
@patch("time.sleep", return_value=None)
def test_make_request_rate_limit_retry(mock_sleep):
    # First request returns 403 rate limit, second succeeds
    responses.add(
        responses.GET, "https://api.github.com/test", status=403, headers={"Retry-After": "1"}
    )
    responses.add(responses.GET, "https://api.github.com/test", json={"status": "ok"}, status=200)

    resp = make_request("https://api.github.com/test", headers={})
    assert resp.status_code == 200
    assert mock_sleep.call_count == 1
    mock_sleep.assert_called_with(1)


@responses.activate
def test_make_request_rate_limit_abort():
    responses.add(
        responses.GET, "https://api.github.com/test", status=403, headers={"Retry-After": "1000"}
    )
    state.abort_flag = False

    with pytest.raises(RateLimitExceededError):
        make_request("https://api.github.com/test", headers={})

    assert state.abort_flag is True


@responses.activate
def test_fetchjson_success():
    responses.add(responses.GET, "https://api.github.com/test", json={"data": 123}, status=200)
    data = fetchjson("https://api.github.com/test")
    assert data == {"data": 123}


@responses.activate
def test_fetchjson_failure():
    responses.add(responses.GET, "https://api.github.com/test", status=404)
    data = fetchjson("https://api.github.com/test")
    assert data == {}


@responses.activate
def test_fetch_schema_with_etag_200():
    valid_schema = {"$schema": "http://json-schema.org/draft-07/schema#", "properties": {}}
    # 600 bytes to pass size validation
    large_schema = json.dumps(valid_schema) + " " * 600
    responses.add(
        responses.GET,
        "https://api.github.com/schema",
        body=large_schema,
        status=200,
        headers={"ETag": "W/123"},
    )

    cache = {}
    schema = fetch_schema_with_etag("https://api.github.com/schema", "my_schema", cache)
    assert schema == valid_schema
    assert cache["my_schema"]["etag"] == "W/123"


@responses.activate
def test_fetch_schema_with_etag_304():
    responses.add(responses.GET, "https://api.github.com/schema", status=304)

    cache = {"my_schema": {"etag": "W/123", "schema": {"cached": True}}}
    schema = fetch_schema_with_etag("https://api.github.com/schema", "my_schema", cache)
    assert schema == {"cached": True}


@responses.activate
def test_fetch_schema_with_etag_invalid_size():
    responses.add(responses.GET, "https://api.github.com/schema", body="{}", status=200)
    cache = {"my_schema": {"schema": {"last_good": True}}}
    schema = fetch_schema_with_etag("https://api.github.com/schema", "my_schema", cache)
    assert schema == {"last_good": True}
