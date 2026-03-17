from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # NOTE: Update locators to match AUT
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    REGISTER_LINK = (By.LINK_TEXT, "Register")

    def go_to_login(self, base_url):
        self.open(base_url)

    def login(self, email, password):
        self.type(*self.EMAIL_INPUT, text=email)
        self.type(*self.PASSWORD_INPUT, text=password)
        self.click(*self.LOGIN_BUTTON)

    def is_logged_in(self):
        # Placeholder: check for user avatar or logout link
        try:
            self.find(By.CSS_SELECTOR, "a.logout")
            return True
        except Exception:
            return False
