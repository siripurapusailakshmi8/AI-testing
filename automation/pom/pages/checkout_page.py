from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    ADDRESS_INPUT = (By.NAME, "address")
    PAYMENT_METHOD = (By.CSS_SELECTOR, ".payment-method")
    PAY_BUTTON = (By.CSS_SELECTOR, "button.pay")

    def enter_address(self, address):
        self.type(*self.ADDRESS_INPUT, text=address)

    def select_payment_method(self, method_name):
        methods = self.driver.find_elements(*self.PAYMENT_METHOD)
        for m in methods:
            if method_name.lower() in m.text.lower():
                m.click()
                return True
        return False

    def pay(self):
        self.click(*self.PAY_BUTTON)
