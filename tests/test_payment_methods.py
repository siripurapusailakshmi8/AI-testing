import os
import pytest
from pages.login_page import LoginPage
from pages.restaurant_page import RestaurantPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.order_page import OrderPage

PAYMENT_METHODS = [
    ("card", "test_card"),
    ("upi", "test_upi"),
    ("wallet", "test_wallet"),
]

@pytest.mark.payment
@pytest.mark.parametrize("label,method_value", PAYMENT_METHODS)
def test_payment_method(driver, base_url, label, method_value):
    driver.get(base_url)
    login = LoginPage(driver)
    rest = RestaurantPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    order = OrderPage(driver)

    username = os.getenv("TEST_USER")
    password = os.getenv("TEST_PASSWORD")
    if not username or not password:
        pytest.skip("TEST_USER/TEST_PASSWORD not set")

    # prepare a simple order
    login.login(username, password)
    rest.search_and_open_restaurant(os.getenv("TEST_RESTAURANT", "Test Restaurant"))
    rest.add_first_item_to_cart()
    rest.open_cart()
    cart.proceed_to_checkout()
    checkout.select_address()
    # choose payment method under test
    checkout.select_payment_method(os.getenv(method_value, method_value))
    checkout.pay()

    # verify transaction id is present in order details (best effort)
    driver.implicitly_wait(3)
    try:
        tx = order.get_order_id()
    except Exception:
        pytest.fail("Order/transaction identifier not found after payment")

    # In an actual environment we'd verify payment logs and that no sensitive data is stored.
    assert tx
