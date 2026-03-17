from selenium.webdriver.common.by import By
from .base_page import BasePage

class RestaurantPage(BasePage):
    MENU_ITEM = (By.CSS_SELECTOR, ".menu-item")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".add-to-cart")
    CART_BUTTON = (By.CSS_SELECTOR, "a[href*='cart']")

    def add_first_n_items(self, n=1):
        items = self.driver.find_elements(*self.MENU_ITEM)
        for i in range(min(n, len(items))):
            btn = items[i].find_element(*self.ADD_TO_CART_BUTTON)
            btn.click()

    def go_to_cart(self):
        self.click(*self.CART_BUTTON)
