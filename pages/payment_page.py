from selenium.webdriver.common.by import By
from .base_page import BasePage


class PaymentPage(BasePage):
    """Payment flow helpers (sandbox interactions)"""

    CARD_NUMBER = (By.NAME, "card_number")
    SUBMIT_PAYMENT = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver, base_url=None):
        super().__init__(driver, base_url)

"}