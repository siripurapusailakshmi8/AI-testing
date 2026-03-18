from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.login_btn = (By.ID, "loginBtn")

    def open_url(self):
        self.driver.get("https://example.com/login")

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()
