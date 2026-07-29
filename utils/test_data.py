"""Test data constants for test automation."""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class TestData:
    """Test data constants."""

    # Credentials
    username = os.getenv("TEST_USERNAME", "standard_user")
    password = os.getenv("TEST_PASSWORD", "secret_sauce")

    # URLs
    base_url = os.getenv("BASE_URL", "https://www.saucedemo.com/")
    login_url = os.getenv("LOGIN_URL", "https://example.com/login")

    # Test User Data
    first_name = "Sai"
    last_name = "Lakshmi"
    postal_code = "500010"

    # FAQ Test Data
    question = "What is Selenium?"
    answer = "Selenium is a web automation tool"

    # Other test data
    valid_email = "test@example.com"
    invalid_email = "invalid_email"
    valid_phone = "1234567890"
    invalid_phone = "123"


class BrowserConfig:
    """Browser configuration constants."""

    browser = os.getenv("BROWSER", "chrome").lower()
    headless = os.getenv("HEADLESS", "false").lower() == "true"
    width = int(os.getenv("WINDOW_WIDTH", 1920))
    height = int(os.getenv("WINDOW_HEIGHT", 1080))
    wait_time = int(os.getenv("WAIT_TIME", 10))
    implicit_wait = int(os.getenv("IMPLICIT_WAIT", 5))
    page_load_timeout = int(os.getenv("PAGE_LOAD_TIMEOUT", 15))


class EnvironmentConfig:
    """Environment configuration."""

    environment = os.getenv("ENVIRONMENT", "staging")
    debug = os.getenv("DEBUG", "false").lower() == "true"
    log_level = os.getenv("LOG_LEVEL", "INFO")
