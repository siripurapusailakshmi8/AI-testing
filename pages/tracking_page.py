from selenium.webdriver.common.by import By
from .base_page import BasePage


class TrackingPage(BasePage):
    """Order tracking page skeleton"""

    MAP_MARKER = (By.CSS_SELECTOR, ".map-marker")
    ETA = (By.CSS_SELECTOR, ".eta")

    def __init__(self, driver, base_url=None):
        super().__init__(driver, base_url)

"}