import os
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.restaurant_page import RestaurantPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.order_confirmation_page import OrderConfirmationPage
from pages.order_history_page import OrderHistoryPage


@pytest.mark.AIP60
def test_ofd_ts_001(driver, base_url):
    """Verify end-to-end happy-path order placement by a registered customer."""
    username = os.getenv("TEST_USER", "testuser@example.com")
    password = os.getenv("TEST_PASS", "Password123")
    restaurant_name = os.getenv("TEST_RESTAURANT", "Testaurant")

    login = LoginPage(driver)
    home = HomePage(driver)
    rest = RestaurantPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    confirm = OrderConfirmationPage(driver)
    history = OrderHistoryPage(driver)

    # 1. Login
    login.open_url(f"{base_url}/login")
    login.login(username, password)

    # 2. Navigate to restaurant
    home.go_to_home(base_url)
    home.open_restaurant_by_name(restaurant_name)

    # 3. Add items
    rest.add_first_item_to_cart(quantity=1)

    # 4. Go to checkout
    cart.go_to_checkout()
    assert checkout.confirm_address() is not None

    # 5. Select sandbox payment method and complete
    checkout.select_payment_method("Sandbox")
    checkout.complete_payment()

    # 6. Submit order - in this simplified flow complete_payment triggers submit

    # 7. Capture order id from confirmation
    order_id = confirm.get_order_id()
    assert order_id, "Order ID should be present on confirmation"

    # 8. Navigate to order history and validate
    history.open_latest_order()
    hist_id = history.get_latest_order_id()
    assert order_id == hist_id, "Order ID in history should match confirmation"
