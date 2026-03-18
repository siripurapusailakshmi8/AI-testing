from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    ADDRESS_SELECT = (By.CSS_SELECTOR, "select.address-select")
    PAYMENT_METHOD = (By.CSS_SELECTOR, "input[name='payment-method']")
    PAY_BUTTON = (By.CSS_SELECTOR, "button.pay-now")

    def select_address(self):
        # select first address
        self.click(*self.ADDRESS_SELECT)

    def select_payment_method(self, method_value):
        # method_value expected to match input value attribute
        self.click(By.CSS_SELECTOR, f"input[name='payment-method'][value='{method_value}']")

    def pay(self):
        self.click(*self.PAY_BUTTON)
