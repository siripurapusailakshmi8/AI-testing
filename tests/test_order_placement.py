import os
import time
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.restaurant_page import RestaurantPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.order_page import OrderPage


@pytest.mark.smoke
def test_end_to_end_order_placement(driver, base_url, test_user):
    """OFD-TC-001: End-to-end order placement"""
    login = LoginPage(driver, base_url)
    login.open('/login')
    login.type(*LoginPage.USERNAME, test_user['username'])
    login.type(*LoginPage.PASSWORD, test_user['password'])
    login.click(*LoginPage.SUBMIT)

    home = HomePage(driver, base_url)
    # navigate to a restaurant - this is a simplified flow and may need selectors updated
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
    checkout.click(*CheckoutPage.PLACE_ORDER)

    # assume redirect to order page
    order = OrderPage(driver, base_url)
    order_id = order.get_text(*OrderPage.ORDER_ID)
    assert order_id, "Order ID should be present"

    # basic API check (requires environment variable ORDER_API_BASE)
    order_api = os.environ.get('ORDER_API_BASE')
    if order_api and order_id:
        import requests
        resp = requests.get(f"{order_api}/orders/{order_id}")
        assert resp.status_code == 200
        data = resp.json()
        assert data.get('status') in ('PLACED','CONFIRMED')
        assert data.get('payment_status') in ('PAID','SUCCESS')

"}