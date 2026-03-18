from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def click(self, by, locator):
        el = self.find(by, locator)
        el.click()

    def send_keys(self, by, locator, keys):
        el = self.find(by, locator)
        el.clear()
        el.send_keys(keys)

    def get_text(self, by, locator):
        el = self.find(by, locator)
        return el.text
