import maintenance.state as state
from maintenance.config import get_config
from maintenance.github_crawler import fetch_schemas, main

MOCK_CONFIG = get_config("scoop_shovel")


def test_fetch_schemas(mocker):
    mock_fetch = mocker.patch("maintenance.github_crawler.fetch_schema_with_etag")
    mock_fetch.side_effect = ["scoop_schema_mock", "shovel_schema_mock"]

    cache = {}
    fetch_schemas(cache, MOCK_CONFIG)

    assert state.SCHEMAS["scoop"] == "scoop_schema_mock"
    assert state.SCHEMAS["shovel"] == "shovel_schema_mock"
    assert mock_fetch.call_count == 2


def test_main(mocker, tmp_path):
    # Mock everything that main calls to prevent real execution
    mocker.patch("maintenance.github_crawler.load_dotenv")
    mocker.patch("maintenance.github_crawler.dir_path", str(tmp_path))

    mock_load_cache = mocker.patch("maintenance.github_crawler.load_cache", return_value={})
    mock_fetch_schemas = mocker.patch("maintenance.github_crawler.fetch_schemas")
    mock_discover = mocker.patch("maintenance.github_crawler.discover_repositories")
    mock_update = mocker.patch("maintenance.github_crawler.update_repositories")
    mock_save_cache = mocker.patch("maintenance.github_crawler.save_cache")

    mock_metrics = mocker.patch("maintenance.github_crawler.calculate_metrics")
    mock_metrics.return_value = ([], [], [], [], [], {})
    mock_readme = mocker.patch("maintenance.github_crawler.generate_readme")
    mock_apis = mocker.patch("maintenance.github_crawler.generate_apis")

    main()

    # Assert all the high-level orchestrated phases were called for both ecosystems
    assert mock_load_cache.call_count == 3
    assert mock_fetch_schemas.call_count == 3
    assert mock_discover.call_count == 3
    assert mock_update.call_count == 3
    assert mock_save_cache.call_count == 6
    assert mock_metrics.call_count == 3
    assert mock_readme.call_count == 3
    assert mock_apis.call_count == 3
