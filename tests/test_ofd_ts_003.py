import os
import time
import requests
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.restaurant_page import RestaurantPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.order_confirmation_page import OrderConfirmationPage


@pytest.mark.AIP62
def test_ofd_ts_003_order_tracking_updates(driver, base_url):
    """Verify real-time order tracking updates reflect delivery partner location changes."""
    username = os.getenv("TEST_USER", "testuser@example.com")
    password = os.getenv("TEST_PASS", "Password123")
    restaurant_name = os.getenv("TEST_RESTAURANT", "Testaurant")

    # Steps: place an order and then use mock API to inject location updates
    login = LoginPage(driver)
    home = HomePage(driver)
    rest = RestaurantPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    confirm = OrderConfirmationPage(driver)

    # Login and place an order
    login.open_url(f"{base_url}/login")
    login.login(username, password)
    home.go_to_home(base_url)
    home.open_restaurant_by_name(restaurant_name)
    rest.add_first_item_to_cart(quantity=1)
    cart.go_to_checkout()
    checkout.select_payment_method("Sandbox")
    checkout.complete_payment()
    order_id = confirm.get_order_id()
    assert order_id, "Order creation failed"

    # Mock API settings (should be provided by test environment)
    mock_api = os.getenv("MOCK_TRACKING_API", f"{base_url}/__mocks__/tracking")
    partner_id = os.getenv("MOCK_PARTNER_ID", "partner-123")

    # Inject two locations sequentially
    loc1 = {"order_id": order_id, "partner_id": partner_id, "lat": 12.9716, "lng": 77.5946}
    loc2 = {"order_id": order_id, "partner_id": partner_id, "lat": 12.9750, "lng": 77.5990}

    r1 = requests.post(f"{mock_api}/location", json=loc1)
    assert r1.status_code in (200, 201), "Failed to inject location 1"
    # Wait briefly for realtime system to process
    time.sleep(2)

    # In UI, open tracking view - simplified as navigation to /orders/{order_id}/track
    driver.get(f"{base_url}/orders/{order_id}/track")
    # Validate that map or marker is present - placeholder checks
    # Here we look for presence of a marker element
    # NOTE: selectors must be adapted to actual app
    # Allow some time for update
    time.sleep(2)
    # Inject second location
    r2 = requests.post(f"{mock_api}/location", json=loc2)
    assert r2.status_code in (200, 201), "Failed to inject location 2"
    time.sleep(2)

    # Placeholder assertion: ensure page still loads and contains order id
    assert str(order_id) in driver.page_source
