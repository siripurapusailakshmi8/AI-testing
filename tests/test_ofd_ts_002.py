import os
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.restaurant_page import RestaurantPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.order_confirmation_page import OrderConfirmationPage


@pytest.mark.AIP61
def test_ofd_ts_002_payment_methods(driver, base_url):
    """Verify secure payment processing for multiple payment methods using sandbox."""
    username = os.getenv("TEST_USER", "testuser@example.com")
    password = os.getenv("TEST_PASS", "Password123")
    restaurant_name = os.getenv("TEST_RESTAURANT", "Testaurant")

    login = LoginPage(driver)
    home = HomePage(driver)
    rest = RestaurantPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    confirm = OrderConfirmationPage(driver)

    login.open_url(f"{base_url}/login")
    login.login(username, password)

    home.go_to_home(base_url)
    home.open_restaurant_by_name(restaurant_name)
    rest.add_first_item_to_cart(quantity=1)
    cart.go_to_checkout()

    payment_methods = ["Card", "UPI", "Wallet"]
    for method in payment_methods:
        # For each method, attempt to select and complete payment
        checkout.select_payment_method(method)
        checkout.complete_payment()
        order_id = confirm.get_order_id()
        assert order_id, f"Order ID should be present for payment method {method}"
        # Ideally verify transaction id / payment status via API; placeholder assertion here
        # Navigate back to home to repeat for next method (or clear cart)
        home.go_to_home(base_url)
        home.open_restaurant_by_name(restaurant_name)
        rest.add_first_item_to_cart(quantity=1)
        cart.go_to_checkout()
