from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 20)

    def open(self, path=""):
        url = self.base_url.rstrip('/') + '/' + path.lstrip('/')
        self.driver.get(url)

    def find(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def find_all(self, by, locator):
        return self.wait.until(EC.presence_of_all_elements_located((by, locator)))

    def click(self, by, locator):
        el = self.wait.until(EC.element_to_be_clickable((by, locator)))
        el.click()

    def type(self, by, locator, text):
        el = self.find(by, locator)
        el.clear()
        el.send_keys(text)

    def wait_for_text(self, by, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element((by, locator), text))
