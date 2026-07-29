"""WebDriver factory for creating browser instances."""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from utils.logger import get_logger
from utils.test_data import BrowserConfig

logger = get_logger(__name__)


def get_driver(browser: str = None):
    """Create and return WebDriver instance.
    
    Args:
        browser: Browser type ('chrome' or 'firefox'). Defaults to config.
        
    Returns:
        WebDriver: Configured Selenium WebDriver instance
    """
    browser = browser or BrowserConfig.browser
    logger.info(f"Creating WebDriver for browser: {browser}")

    if browser.lower() == "chrome":
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

    elif browser.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        if BrowserConfig.headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options,
        )
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    # Set timeouts
    driver.set_page_load_timeout(BrowserConfig.page_load_timeout)
    driver.implicitly_wait(BrowserConfig.implicit_wait)

    logger.info("WebDriver initialized successfully")
    return driver


def quit_driver(driver):
    """Quit WebDriver and cleanup resources.
    
    Args:
        driver: WebDriver instance to quit
    """
    logger.info("Closing WebDriver")
    driver.quit()
    logger.info("WebDriver closed successfully")
