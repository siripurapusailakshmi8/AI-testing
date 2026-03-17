from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "button.checkout")
    ITEM_ROW = (By.CSS_SELECTOR, ".cart-item")
    TOTAL_PRICE = (By.CSS_SELECTOR, ".cart-total")

    def get_item_count(self):
        return len(self.driver.find_elements(*self.ITEM_ROW))

    def get_total(self):
        return self.get_text(*self.TOTAL_PRICE)

    def proceed_to_checkout(self):
        self.click(*self.CHECKOUT_BUTTON)
