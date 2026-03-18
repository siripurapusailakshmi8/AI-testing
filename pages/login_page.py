from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    """Page object for login page - initial skeleton."""

    # locators
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver, base_url=None):
        super().__init__(driver, base_url)

    # TODO: Add helper methods like login

"}