from selenium.webdriver.common.by import By
from .base_page import BasePage

class RestaurantPage(BasePage):
    MENU_ITEM = (By.CSS_SELECTOR, '.menu-item')
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.add-to-cart')

    def add_first_item_to_cart(self):
        items = self.find_all(*self.MENU_ITEM)
        if items:
            items[0].find_element(*self.ADD_TO_CART_BTN).click()
