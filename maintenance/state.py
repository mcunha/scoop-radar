"""Global state for the maintenance crawler."""

abort_flag = False
SCHEMAS = {}
api_retries = 0
evicted_count = 0
evicted_repos = []
