from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_INPUT = (By.NAME, "q")
    RESTAURANT_CARD = (By.CSS_SELECTOR, ".restaurant-card")

    def search_restaurant(self, name):
        self.type(*self.SEARCH_INPUT, text=name)
        self.find(*self.RESTAURANT_CARD)

    def open_first_restaurant(self):
        el = self.find(*self.RESTAURANT_CARD)
        el.click()
