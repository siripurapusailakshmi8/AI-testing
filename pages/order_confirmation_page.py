from selenium.webdriver.common.by import By
from .base_page import BasePage

class OrderConfirmationPage(BasePage):
    """Order confirmation page actions."""

    ORDER_ID = (By.CSS_SELECTOR, ".order-id")
    CONFIRM_MSG = (By.CSS_SELECTOR, ".confirmation-message")

    def get_order_id(self):
        return self.get_text(*self.ORDER_ID)

    def confirmation_message_present(self):
        return self.get_text(*self.CONFIRM_MSG)
