import os
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.restaurant_page import RestaurantPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.order_page import OrderPage


@pytest.mark.parametrize('method', ['card','upi','wallet'])
def test_payment_methods(driver, base_url, test_user, method):
    """OFD-TC-003: Payment processing across methods"""
    login = LoginPage(driver, base_url)
    login.open('/login')
    login.type(*LoginPage.USERNAME, test_user['username'])
    login.type(*LoginPage.PASSWORD, test_user['password'])
    login.click(*LoginPage.SUBMIT)

    home = HomePage(driver, base_url)
    home.open('/restaurants')
    home.click(*HomePage.RESTAURANT_LINK)

    rest = RestaurantPage(driver, base_url)
    rest.click(*RestaurantPage.MENU_ITEM)
    rest.click(*RestaurantPage.ADD_TO_CART)
    rest.click(*RestaurantPage.CART_ICON)

    cart = CartPage(driver, base_url)
    cart.click(*CartPage.CHECKOUT_BUTTON)

    checkout = CheckoutPage(driver, base_url)
    checkout.type(*CheckoutPage.ADDRESS_INPUT, test_user['address'])
    checkout.click(*CheckoutPage.PAYMENT_OPTION)

    payment = PaymentPage(driver, base_url)
    if method == 'card':
        payment.type(*PaymentPage.CARD_NUMBER, os.environ.get('TEST_CARD_NUMBER','4111111111111111'))
    # UPI/Wallet flows would need additional implementation in a real app
    payment.click(*PaymentPage.SUBMIT_PAYMENT)

    order = OrderPage(driver, base_url)
    order_id = order.get_text(*OrderPage.ORDER_ID)
    assert order_id

    # optional API validation
    order_api = os.environ.get('ORDER_API_BASE')
    if order_api:
        import requests
        resp = requests.get(f"{order_api}/orders/{order_id}")
        assert resp.status_code == 200
        data = resp.json()
        assert data.get('payment_status') in ('PAID','SUCCESS')

"}