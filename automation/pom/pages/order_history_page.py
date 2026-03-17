from selenium.webdriver.common.by import By
from .base_page import BasePage

class OrderHistoryPage(BasePage):
    ORDER_ROW = (By.CSS_SELECTOR, ".order-row")

    def has_order(self, order_id_or_text):
        orders = self.driver.find_elements(*self.ORDER_ROW)
        for o in orders:
            if order_id_or_text in o.text:
                return True
        return False
