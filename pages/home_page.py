from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_BOX = (By.NAME, 'q')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button.search')
    RESTAURANT_LIST = (By.CSS_SELECTOR, '.restaurant-item')

    def open_home(self):
        self.open('/')

    def search_restaurant(self, name):
        self.type(*self.SEARCH_BOX, name)
        self.click(*self.SEARCH_BUTTON)

    def get_restaurants(self):
        return self.finds(*self.RESTAURANT_LIST)
