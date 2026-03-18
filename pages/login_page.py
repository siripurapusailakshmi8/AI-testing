from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    SUBMIT = (By.CSS_SELECTOR, 'button[type="submit"]')

    def open_login(self):
        self.open('/login')

    def login(self, email, password):
        self.type(*self.EMAIL, email)
        self.type(*self.PASSWORD, password)
        self.click(*self.SUBMIT)
