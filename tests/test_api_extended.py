import json
from unittest.mock import patch

import responses

from maintenance.api import fetch_schema_with_etag, make_request
from maintenance.config import get_config

MOCK_CONFIG = get_config("scoop_shovel")


@responses.activate
@patch("time.sleep", return_value=None)
@patch("time.time", return_value=1000)
def test_make_request_rate_limit_x_ratelimit(mock_time, mock_sleep):
    responses.add(
        responses.GET,
        "https://api.github.com/test",
        status=403,
        headers={"X-RateLimit-Remaining": "0", "X-RateLimit-Reset": "1005"},
    )
    responses.add(responses.GET, "https://api.github.com/test", json={"status": "ok"}, status=200)

    resp = make_request("https://api.github.com/test", headers={})
    assert resp.status_code == 200
    mock_sleep.assert_called_with(6)


@responses.activate
@patch("time.sleep", return_value=None)
def test_make_request_rate_limit_secondary(mock_sleep):
    responses.add(responses.GET, "https://api.github.com/test", status=429)
    responses.add(responses.GET, "https://api.github.com/test", json={"status": "ok"}, status=200)

    resp = make_request("https://api.github.com/test", headers={})
    assert resp.status_code == 200
    mock_sleep.assert_called_with(60)


@responses.activate
def test_fetch_schema_with_etag_invalid_structure():
    invalid_schema = {"invalid": "schema"}
    large_schema = json.dumps(invalid_schema) + " " * 600
    responses.add(responses.GET, "https://api.github.com/schema", body=large_schema, status=200)

    cache = {"my_schema": {"schema": {"last_good": True}}}
    schema = fetch_schema_with_etag("https://api.github.com/schema", "my_schema", cache)
    assert schema == {"last_good": True}


@responses.activate
def test_fetch_schema_with_etag_exception():
    responses.add(
        responses.GET, "https://api.github.com/schema", body=Exception("Connection Failed")
    )

    cache = {"my_schema": {"schema": {"last_good": True}}}
    schema = fetch_schema_with_etag("https://api.github.com/schema", "my_schema", cache)
    assert schema == {"last_good": True}
