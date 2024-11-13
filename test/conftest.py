import pytest
from snowflake.snowpark.session import Session


def pytest_addoption(parser):
    parser.addoption("--snowflake-session", action="store", default="live")

@pytest.fixture
def session(request) -> Session:
    if request.config.getoption('--snowflake-session') == 'local':
        return Session.builder.configs({'local_testing': True}).create()
    else:
        return Session.builder.getOrCreate()
    #return Session.builder.configs(get_env_var_config()).create()