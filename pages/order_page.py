from selenium.webdriver.common.by import By
from .base_page import BasePage

class OrderPage(BasePage):
    ORDER_ID = (By.CSS_SELECTOR, "#order-id")
    ORDER_STATUS = (By.CSS_SELECTOR, "#order-status")

    def get_order_id(self):
        return self.get_text(*self.ORDER_ID)

    def get_order_status(self):
        return self.get_text(*self.ORDER_STATUS)
