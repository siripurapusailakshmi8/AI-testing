from selenium.webdriver.common.by import By
from .base_page import BasePage

class RestaurantPage(BasePage):
    MENU_ITEM = (By.CSS_SELECTOR, '.menu-item')
    ADD_TO_CART = (By.CSS_SELECTOR, 'button.add-to-cart')

    def open_restaurant(self, rest_path):
        self.open(rest_path)

    def add_first_item_to_cart(self):
        items = self.finds(*self.MENU_ITEM)
        if not items:
            raise Exception('No menu items found')
        # Click add to cart of first item
        self.click(*self.ADD_TO_CART)
