import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.restaurant_page import RestaurantPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.orders_page import OrdersPage

@pytest.mark.smoke
def test_end_to_end_order_flow(driver, base_url):
    # Note: This test assumes a testable staging environment. Update selectors and data as needed.
    home = HomePage(driver, base_url)
    login = LoginPage(driver, base_url)
    rest = RestaurantPage(driver, base_url)
    cart = CartPage(driver, base_url)
    checkout = CheckoutPage(driver, base_url)
    orders = OrdersPage(driver, base_url)

    home.open_home()
    # Try login (if login page present); otherwise assume guest flow
    try:
        login.open_login()
        login.login('testuser@example.com', 'Password123')
    except Exception:
        # If login not present, continue
        pass

    # Search and open restaurant
    home.search_restaurant('Testaurant')
    restaurants = home.get_restaurants()
    assert restaurants, 'No restaurants found'
    # Open first restaurant (click)
    restaurants[0].click()

    # Add item to cart
    rest.add_first_item_to_cart()
    cart.open_cart()
    assert cart.get_cart_items(), 'Cart is empty after adding item'

    # Checkout
    cart.proceed_to_checkout()
    checkout.fill_address('123 Test Street')
    checkout.select_payment('sandbox-card')
    checkout.place_order()

    # Verify order in orders page
    orders.open_orders()
    assert orders.get_orders(), 'No orders found in My Orders'
