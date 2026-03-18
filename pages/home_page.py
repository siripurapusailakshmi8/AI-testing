from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    """Home/Browse page actions."""

    # Example locators - these should be adjusted to the actual application's selectors
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[placeholder='Search']")
    RESTAURANT_CARD = (By.CSS_SELECTOR, ".restaurant-card")
    RESTAURANT_NAME = (By.CSS_SELECTOR, ".restaurant-name")

    def go_to_home(self, base_url):
        self.open_url(base_url)

    def search_restaurant(self, name):
        self.type(*self.SEARCH_INPUT, text=name)
        # Wait for results to load
        return self.find(*self.RESTAURANT_CARD)

    def open_restaurant_by_name(self, name):
        cards = self.finds(*self.RESTAURANT_CARD)
        for c in cards:
            try:
                title = c.find_element(*self.RESTAURANT_NAME).text
                if name.lower() in title.lower():
                    c.click()
                    return
            except Exception:
                continue
        raise Exception(f"Restaurant with name '{name}' not found")
