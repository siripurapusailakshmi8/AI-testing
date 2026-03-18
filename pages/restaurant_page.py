from selenium.webdriver.common.by import By
from .base_page import BasePage

class RestaurantPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[placeholder='Search']")
    RESTAURANT_LINK = (By.CSS_SELECTOR, "a.restaurant-item")
    MENU_ITEM_ADD = (By.CSS_SELECTOR, "button.add-item")
    VIEW_CART = (By.CSS_SELECTOR, "a.view-cart")

    def search_and_open_restaurant(self, name):
        self.send_keys(*self.SEARCH_INPUT, keys=name)
        # simple click first result
        self.click(*self.RESTAURANT_LINK)

    def add_first_item_to_cart(self):
        self.click(*self.MENU_ITEM_ADD)

    def open_cart(self):
        self.click(*self.VIEW_CART)
