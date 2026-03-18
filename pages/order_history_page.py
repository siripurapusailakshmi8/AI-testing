from selenium.webdriver.common.by import By
from .base_page import BasePage

class OrderHistoryPage(BasePage):
    """Order history page actions."""

    LATEST_ORDER = (By.CSS_SELECTOR, ".order-row")
    ORDER_ID = (By.CSS_SELECTOR, ".order-id")

    def open_latest_order(self):
        self.click(*self.LATEST_ORDER)

    def get_latest_order_id(self):
        return self.get_text(*self.ORDER_ID)
