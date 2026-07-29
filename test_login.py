"""Login functionality tests."""

import pytest
from pages.login_page import LoginPage
from utils.test_data import TestData
from utils.logger import get_logger

logger = get_logger(__name__)


class TestLogin:
    """Test suite for Login functionality."""

    @pytest.mark.smoke
    def test_valid_login(self, driver):
        """Test login with valid credentials.
        
        Steps:
            1. Open login page
            2. Enter valid username and password
            3. Click login button
            4. Verify dashboard is displayed
        """
        logger.info("Starting test_valid_login")
        login = LoginPage(driver)

        login.open_url()
        login.login(TestData.username, TestData.password)

        assert "dashboard" in driver.current_url, "Dashboard URL not found after login"
        logger.info("Test passed: Valid login successful")

    @pytest.mark.regression
    def test_invalid_password_login(self, driver):
        """Test login with invalid password."""
        logger.info("Starting test_invalid_password_login")
        login = LoginPage(driver)

        login.open_url()
        login.login(TestData.username, "invalid_password")

        error_msg = login.get_error_message()
        assert error_msg is not None, "Expected error message not found"
        logger.info("Test passed: Invalid password rejection working")

    @pytest.mark.regression
    def test_empty_credentials_login(self, driver):
        """Test login with empty credentials."""
        logger.info("Starting test_empty_credentials_login")
        login = LoginPage(driver)

        login.open_url()
        login.login("", "")

        error_msg = login.get_error_message()
        assert error_msg is not None, "Expected error message for empty credentials"
        logger.info("Test passed: Empty credentials rejection working")
