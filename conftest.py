import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def base_url():
    # Override via environment variable QA_BASE_URL
    return os.getenv("QA_BASE_URL", "https://staging.example.com")


@pytest.fixture(scope="function")
def driver():
    """Create a Chrome webdriver instance. Adjust for your CI (chromedriver location, remote webdriver, etc.)"""
    chrome_options = Options()
    if os.getenv("HEADLESS", "1") == "1":
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    try:
        driver.quit()
    except Exception:
        pass
