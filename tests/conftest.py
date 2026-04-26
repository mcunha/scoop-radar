import pytest

import maintenance.state as state


@pytest.fixture(autouse=True)
def reset_state():
    state.abort_flag = False
    state.SCHEMAS = {}
