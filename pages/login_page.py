from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # NOTE: Locators below are placeholders and must be adapted to the AUT.
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type=submit]")

    def login(self, username, password):
        self.send_keys(*self.USERNAME, keys=username)
        self.send_keys(*self.PASSWORD, keys=password)
        self.click(*self.LOGIN_BUTTON)
