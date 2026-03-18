from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    """Login page actions."""

    USER_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASS_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    def login(self, username, password):
        self.type(*self.USER_INPUT, text=username)
        self.type(*self.PASS_INPUT, text=password)
        self.click(*self.SUBMIT_BTN)
