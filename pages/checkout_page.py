from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    """Checkout and payment page actions."""

    ADDRESS_CONFIRM = (By.CSS_SELECTOR, ".address-confirm")
    PAYMENT_METHODS = (By.CSS_SELECTOR, ".payment-method")
    PAY_BUTTON = (By.CSS_SELECTOR, ".pay-button")

    def confirm_address(self):
        # Typically a no-op if address already shown; left here to validate presence
        return self.find(*self.ADDRESS_CONFIRM)

    def select_payment_method(self, method_name):
        methods = self.finds(*self.PAYMENT_METHODS)
        for m in methods:
            if method_name.lower() in m.text.lower():
                m.click()
                return
        raise Exception(f"Payment method '{method_name}' not found")

    def complete_payment(self):
        self.click(*self.PAY_BUTTON)
        # In sandbox modes, additional flows (iframe/redirect) might be needed - those should be handled by test config
