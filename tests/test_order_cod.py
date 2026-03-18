import time
import requests
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.restaurant_page import RestaurantPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.order_page import OrderPage


def test_place_order_cod(driver, base_url, api_client, test_user):
    login = LoginPage(driver, base_url)
    home = HomePage(driver, base_url)
    rest = RestaurantPage(driver, base_url)
    cart = CartPage(driver, base_url)
    checkout = CheckoutPage(driver, base_url)
    order = OrderPage(driver, base_url)

    # Step 1-2
    login.open_login()
    login.login(test_user['username'], test_user['password'])

    # Step 3
    home.open_home()
    home.search_restaurant('Test Restaurant')

    # Step 4
    rest.add_first_item_to_cart()
    cart_items = cart.get_cart_items()
    assert len(cart_items) > 0

    # Step 5
    cart.proceed_to_checkout()
    checkout.select_address(0)
    checkout.choose_cod()
    checkout.place_order()

    # Step 6
    order.wait_for_confirmation()
    order_id = order.get_order_id()
    assert order_id

    # Step 7 - notification check (stubbed via API)
    # This assumes a test API endpoint that can be queried for notifications
    notif = api_client.get(f"/notifications?order_id={order_id}")
    assert notif.status_code == 200

    # Step 8 - backend order check
    resp = api_client.get(f"/orders/{order_id}")
    assert resp.status_code == 200
    body = resp.json()
    assert body.get('status') in ('Placed', 'placed')
    assert body.get('payment_method') in ('COD', 'Cash on Delivery', 'cod')
