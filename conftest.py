import pytest
from selenium import webdriver
import requests

@pytest.fixture(scope='session')
def base_url():
    return 'https://qa.example.com'

@pytest.fixture(scope='session')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def api_client():
    class ApiClient:
        base = 'https://qa-api.example.com'
        def get(self, path):
            return requests.get(self.base + path)
        def post(self, path, json=None):
            return requests.post(self.base + path, json=json)
    return ApiClient()

@pytest.fixture(scope='session')
def test_user():
    return {'username': 'testuser', 'password': 'Password123'}

@pytest.fixture(scope='session')
def sandbox_card():
    return {'number': '4111111111111111', 'exp': '12/30', 'cvv': '123'}

@pytest.fixture
def test_order():
    # This fixture should create an order in Accepted state via API
    return {'order_id': 'TEST_ORDER_1234'}
