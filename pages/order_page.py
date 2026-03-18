from selenium.webdriver.common.by import By
from .base_page import BasePage

class OrderPage(BasePage):
    ORDER_ID = (By.CSS_SELECTOR, '.order-id')
    CONFIRMATION = (By.CSS_SELECTOR, '.order-confirmation')

    def get_order_id(self):
        el = self.find(*self.ORDER_ID)
        return el.text

    def wait_for_confirmation(self):
        return self.find(*self.CONFIRMATION)
