from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def find(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def click(self, by, locator):
        el = self.wait.until(EC.element_to_be_clickable((by, locator)))
        el.click()

    def type(self, by, locator, text):
        el = self.find(by, locator)
        el.clear()
        el.send_keys(text)

    def get_text(self, by, locator):
        return self.find(by, locator).text

    def open(self, url):
        self.driver.get(url)
