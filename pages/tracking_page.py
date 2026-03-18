from selenium.webdriver.common.by import By
from .base_page import BasePage

class TrackingPage(BasePage):
    STATUS_TEXT = (By.CSS_SELECTOR, '.tracking-status')
    MAP = (By.CSS_SELECTOR, '.tracking-map')

    def open_tracking(self, order_id):
        self.open(f'/orders/{order_id}/tracking')

    def get_status(self):
        el = self.find(*self.STATUS_TEXT)
        return el.text

    def has_map(self):
        try:
            self.find(*self.MAP)
            return True
        except:
            return False
