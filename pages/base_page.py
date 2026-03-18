from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Basic page interactions and utilities"""

    def __init__(self, driver, base_url: str = None):
        self.driver = driver
        self.base_url = base_url

    def open(self, path: str = ""):
        url = self.base_url.rstrip("/") + "/" + path.lstrip("/") if self.base_url else path
        self.driver.get(url)

    def find(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def finds(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((by, value)))

    def click(self, by, value, timeout=10):
        el = self.find(by, value, timeout)
        el.click()

    def type(self, by, value, text, timeout=10):
        el = self.find(by, value, timeout)
        el.clear()
        el.send_keys(text)

    def wait_for_text(self, by, value, text, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element((by, value), text))

    def current_url(self):
        return self.driver.current_url

    def get_text(self, by, value, timeout=10):
        el = self.find(by, value, timeout)
        return el.text


# Page-specific helpers will extend BasePage

"}