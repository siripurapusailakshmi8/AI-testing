from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, '.cart-item')
    CHECKOUT_BTN = (By.CSS_SELECTOR, 'button.checkout')
    TOTAL = (By.CSS_SELECTOR, '.cart-total')

    def get_cart_items(self):
        return self.find_all(*self.CART_ITEMS)

    def get_total(self):
        el = self.find(*self.TOTAL)
        return el.text

    def proceed_to_checkout(self):
        self.click(*self.CHECKOUT_BTN)
