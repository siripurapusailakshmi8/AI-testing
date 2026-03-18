from selenium.webdriver.common.by import By
from .base_page import BasePage

class OrdersPage(BasePage):
    ORDER_ROWS = (By.CSS_SELECTOR, '.order-row')

    def open_orders(self):
        self.open('/my-orders')

    def get_orders(self):
        return self.finds(*self.ORDER_ROWS)
