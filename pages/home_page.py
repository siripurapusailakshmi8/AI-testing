from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_INPUT = (By.ID, 'search')
    RESTAURANT_CARD = (By.CSS_SELECTOR, '.restaurant-card')

    def open_home(self):
        self.open('/')

    def search_restaurant(self, name):
        self.type(*self.SEARCH_INPUT, text=name)
        # simple select first result
        cards = self.find_all(*self.RESTAURANT_CARD)
        if cards:
            cards[0].click()
