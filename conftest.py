import os
import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def base_url():
    return os.environ.get('BASE_URL', 'http://localhost:8000')


@pytest.fixture(scope='session')
def test_user():
    # simple test user provider; in real use, fetch from secret store or test data service
    return {
        'username': os.environ.get('TEST_USERNAME', 'testuser'),
        'password': os.environ.get('TEST_PASSWORD', 'password'),
        'address': os.environ.get('TEST_ADDRESS', '123 Test St')
    }


@pytest.fixture()
def driver():
    # use headless Chrome by default
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption('--base-url', action='store', default=os.environ.get('BASE_URL'))

"}