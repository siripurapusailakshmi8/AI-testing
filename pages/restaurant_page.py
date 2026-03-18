from selenium.webdriver.common.by import By
from .base_page import BasePage


class RestaurantPage(BasePage):
    """Restaurant menu page skeleton"""

    MENU_ITEM = (By.CSS_SELECTOR, ".menu-item")
    ADD_TO_CART = (By.CSS_SELECTOR, ".add-to-cart")
    CART_ICON = (By.CSS_SELECTOR, ".cart-icon")

    def __init__(self, driver, base_url=None):
        super().__init__(driver, base_url)

"}