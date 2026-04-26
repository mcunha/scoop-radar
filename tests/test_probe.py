from maintenance.config import get_config
MOCK_CONFIG = get_config('scoop_shovel')

import requests
import responses

from maintenance.probe import extract_urls_from_manifest, probe_url


def test_extract_urls_from_manifest():
    manifest = {
        "version": "1.0",
        "url": "https://example.com/download.zip",
        "architecture": {
            "64bit": {
                "url": ["https://example.com/download64.zip", "http://example.com/invalid$version"]
            },
            "32bit": {
                "url": ["https://example.com/list1.zip", "https://example.com/list2.zip#/dl.7z"]
            },
        },
    }

    urls = extract_urls_from_manifest(manifest)
    assert len(urls) == 4
    assert "https://example.com/download.zip" in urls
    assert "https://example.com/download64.zip" in urls
    assert "https://example.com/list1.zip" in urls
    assert "https://example.com/list2.zip" in urls  # fragment stripped


@responses.activate
def test_probe_url_head_success():
    responses.add(responses.HEAD, "https://example.com/test", status=200)
    assert probe_url("https://example.com/test") is True


@responses.activate
def test_probe_url_head_fallback_get():
    responses.add(responses.HEAD, "https://example.com/test", status=405)
    responses.add(responses.GET, "https://example.com/test", status=200)
    assert probe_url("https://example.com/test") is True


@responses.activate
def test_probe_url_failure():
    responses.add(responses.HEAD, "https://example.com/test", status=404)
    assert probe_url("https://example.com/test") is False


def test_probe_url_request_exception(mocker):
    mocker.patch("requests.head", side_effect=requests.RequestException("Connection Error"))
    assert probe_url("https://example.com/test") is False
