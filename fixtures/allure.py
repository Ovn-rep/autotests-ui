import pytest
from tools.allure.environment import create_environment_properties_dir


@pytest.fixture(scope="session", autouse=True)
def save_allure_environment_file():
    yield
    create_environment_properties_dir()