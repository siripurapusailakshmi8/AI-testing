from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    """Home/Search page object skeleton"""

    SEARCH_INPUT = (By.NAME, "q")
    RESTAURANT_LINK = (By.CSS_SELECTOR, "a.restaurant-link")

    def __init__(self, driver, base_url=None):
        super().__init__(driver, base_url)

"}