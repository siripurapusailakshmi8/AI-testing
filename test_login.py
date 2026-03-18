import pytest
from pages.login_page import LoginPage
from utils.test_data import TestData

def test_valid_login(driver):
    login = LoginPage(driver)

    login.open_url()
    login.login(TestData.username, TestData.password)

    assert "dashboard" in driver.current_url
