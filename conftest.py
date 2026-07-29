"""Pytest configuration and fixtures for test automation."""

import os
import pytest
from pathlib import Path
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from utils.logger import get_logger
from utils.test_data import BrowserConfig, TestData

logger = get_logger(__name__)

# Create screenshots directory
SCREENSHOTS_DIR = Path("screenshots")
SCREENSHOTS_DIR.mkdir(exist_ok=True)


@pytest.fixture(scope="session")
def setup_session():
    """Setup for test session."""
    logger.info("=" * 50)
    logger.info("Test Automation Session Started")
    logger.info(f"Environment: {os.getenv('ENVIRONMENT', 'staging')}")
    logger.info("=" * 50)
    yield
    logger.info("=" * 50)
    logger.info("Test Automation Session Ended")
    logger.info("=" * 50)


@pytest.fixture(scope="function")
def driver():
    """Create and configure WebDriver instance.
    
    Yields:
        WebDriver: Configured Selenium WebDriver instance
    """
    logger.info(f"Creating WebDriver: {BrowserConfig.browser}")

    if BrowserConfig.browser == "chrome":
        options = webdriver.ChromeOptions()
        if BrowserConfig.headless:
            options.add_argument("--headless")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options,
        )

    elif BrowserConfig.browser == "firefox":
        options = webdriver.FirefoxOptions()
        if BrowserConfig.headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options,
        )
    else:
        raise ValueError(f"Unsupported browser: {BrowserConfig.browser}")

    # Set timeouts
    driver.set_page_load_timeout(BrowserConfig.page_load_timeout)
    driver.implicitly_wait(BrowserConfig.implicit_wait)

    # Maximize window
    driver.maximize_window()

    logger.info("WebDriver initialized successfully")

    yield driver

    # Cleanup
    logger.info("Closing WebDriver")
    driver.quit()
    logger.info("WebDriver closed")


@pytest.fixture(autouse=True)
def log_test_info(request):
    """Log test information."""
    logger.info(f"Starting test: {request.node.name}")
    yield
    logger.info(f"Test completed: {request.node.name}")


def pytest_configure(config):
    """Configure pytest."""
    config.addinivalue_line("markers", "smoke: mark test as smoke test")
    config.addinivalue_line("markers", "regression: mark test as regression test")
    config.addinivalue_line("markers", "integration: mark test as integration test")
    logger.info("Pytest configured")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Add custom report info."""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        logger.error(f"Test failed: {item.name}")
        logger.error(f"Error: {rep.longrepr}")


@pytest.fixture
def capture_screenshot(driver):
    """Capture screenshot on demand."""

    def _capture(name: str = None):
        if name is None:
            name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        screenshot_path = SCREENSHOTS_DIR / f"{name}.png"
        driver.save_screenshot(str(screenshot_path))
        logger.info(f"Screenshot saved: {screenshot_path}")
        return screenshot_path

    return _capture
