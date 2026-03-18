from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckoutPage(BasePage):
    """Checkout page skeleton"""

    ADDRESS_INPUT = (By.NAME, "address")
    PAYMENT_OPTION = (By.CSS_SELECTOR, ".payment-option")
    PLACE_ORDER = (By.CSS_SELECTOR, ".place-order")

    def __init__(self, driver, base_url=None):
        super().__init__(driver, base_url)

"}