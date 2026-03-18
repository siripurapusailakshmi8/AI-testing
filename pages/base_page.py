from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Base Page with common helpers for all pages."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_url(self, url):
        self.driver.get(url)

    def find(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def click(self, by, locator):
        elem = self.wait.until(EC.element_to_be_clickable((by, locator)))
        elem.click()

    def type(self, by, locator, text):
        elem = self.wait.until(EC.visibility_of_element_located((by, locator)))
        elem.clear()
        elem.send_keys(text)

    def get_text(self, by, locator):
        elem = self.wait.until(EC.visibility_of_element_located((by, locator)))
        return elem.text

    def wait_for_element(self, by, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, locator)))
