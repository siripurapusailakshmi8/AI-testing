import os
import pytest
from pages.login_page import LoginPage
from pages.restaurant_page import RestaurantPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.order_page import OrderPage

@pytest.mark.end_to_end
def test_end_to_end_ordering(driver, base_url):
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

    # Steps
    login.login(username, password)
    rest.search_and_open_restaurant(os.getenv("TEST_RESTAURANT", "Test Restaurant"))
    rest.add_first_item_to_cart()
    rest.open_cart()
    cart.proceed_to_checkout()
    checkout.select_address()
    checkout.select_payment_method(os.getenv("TEST_PAYMENT_METHOD", "test_card"))
    checkout.pay()

    # NOTE: Many systems redirect to external sandbox - we try to detect order confirmation
    # Wait briefly and assert order confirmation exists
    driver.implicitly_wait(3)
    order_id = None
    try:
        order_id = order.get_order_id()
    except Exception:
        pytest.fail("Order confirmation/order id not found")

    status = order.get_order_status()
    assert status.lower() in ("confirmed", "placed"), f"Unexpected order status: {status}"
    assert order_id
