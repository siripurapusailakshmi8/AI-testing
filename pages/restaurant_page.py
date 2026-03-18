from selenium.webdriver.common.by import By
from .base_page import BasePage

class RestaurantPage(BasePage):
    """Restaurant menu page actions."""

    MENU_ITEM = (By.CSS_SELECTOR, ".menu-item")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".add-to-cart")

    def add_first_item_to_cart(self, quantity=1):
        # Add first available menu item quantity times
        items = self.finds(*self.MENU_ITEM)
        if not items:
            raise Exception("No menu items found")
        first = items[0]
        for _ in range(quantity):
            btn = first.find_element(*self.ADD_TO_CART_BTN)
            btn.click()

    def open_item_by_name(self, name):
        items = self.finds(*self.MENU_ITEM)
        for it in items:
            if name.lower() in it.text.lower():
                it.click()
                return
        raise Exception(f"Menu item '{name}' not found")
