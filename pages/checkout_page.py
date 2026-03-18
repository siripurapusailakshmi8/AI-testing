from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    ADDRESS_SELECT = (By.CSS_SELECTOR, '.address-select')
    PAYMENT_METHOD_COD = (By.ID, 'payment_cod')
    PAYMENT_METHOD_CARD = (By.ID, 'payment_card')
    CARD_NUMBER = (By.ID, 'card_number')
    CARD_EXP = (By.ID, 'card_exp')
    CARD_CVV = (By.ID, 'card_cvv')
    PLACE_ORDER_BTN = (By.CSS_SELECTOR, 'button.place-order')

    def select_address(self, index=0):
        els = self.find_all(*self.ADDRESS_SELECT)
        if els:
            els[index].click()

    def choose_cod(self):
        self.click(*self.PAYMENT_METHOD_COD)

    def choose_card_and_pay(self, number, exp, cvv):
        self.click(*self.PAYMENT_METHOD_CARD)
        self.type(*self.CARD_NUMBER, text=number)
        self.type(*self.CARD_EXP, text=exp)
        self.type(*self.CARD_CVV, text=cvv)

    def place_order(self):
        self.click(*self.PLACE_ORDER_BTN)
