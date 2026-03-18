from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, 'button.checkout')
    CART_ITEMS = (By.CSS_SELECTOR, '.cart-item')

    def open_cart(self):
        self.open('/cart')

    def get_cart_items(self):
        return self.finds(*self.CART_ITEMS)

    def proceed_to_checkout(self):
        self.click(*self.CHECKOUT_BUTTON)
