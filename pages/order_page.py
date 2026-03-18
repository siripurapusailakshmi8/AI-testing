from selenium.webdriver.common.by import By
from .base_page import BasePage


class OrderPage(BasePage):
    """Order confirmation / details page"""

    ORDER_ID = (By.CSS_SELECTOR, ".order-id")
    ORDER_STATUS = (By.CSS_SELECTOR, ".order-status")

    def __init__(self, driver, base_url=None):
        super().__init__(driver, base_url)

"}