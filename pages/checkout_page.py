from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    ADDRESS_SELECTOR = (By.NAME, 'address')
    PAYMENT_METHOD = (By.NAME, 'payment')
    PLACE_ORDER = (By.CSS_SELECTOR, 'button.place-order')

    def fill_address(self, address):
        self.type(*self.ADDRESS_SELECTOR, address)

    def select_payment(self, method):
        self.type(*self.PAYMENT_METHOD, method)

    def place_order(self):
        self.click(*self.PLACE_ORDER)
