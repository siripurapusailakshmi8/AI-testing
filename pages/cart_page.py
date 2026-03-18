from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):
    """Cart page object skeleton"""

    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".btn-checkout")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart-item")

    def __init__(self, driver, base_url=None):
        super().__init__(driver, base_url)

"}