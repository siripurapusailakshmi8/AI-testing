from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self, path=""):
        url = self.base_url.rstrip('/') + '/' + path.lstrip('/')
        self.driver.get(url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def click(self, by, locator):
        self.find(by, locator).click()

    def type(self, by, locator, text):
        el = self.find(by, locator)
        el.clear()
        el.send_keys(text)
