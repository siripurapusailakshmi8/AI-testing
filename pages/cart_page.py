from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    """Cart page actions."""

    CHECKOUT_BTN = (By.CSS_SELECTOR, ".checkout-button")
    CART_ITEM = (By.CSS_SELECTOR, ".cart-item")

    def go_to_checkout(self):
        self.click(*self.CHECKOUT_BTN)

    def get_cart_items(self):
        return self.finds(*self.CART_ITEM)
