from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.restaurant_page import RestaurantPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.order_page import OrderPage


def test_card_payment_flow(driver, base_url, api_client, test_user, sandbox_card):
    login = LoginPage(driver, base_url)
    home = HomePage(driver, base_url)
    rest = RestaurantPage(driver, base_url)
    cart = CartPage(driver, base_url)
    checkout = CheckoutPage(driver, base_url)
    order = OrderPage(driver, base_url)

    login.open_login()
    login.login(test_user['username'], test_user['password'])

    home.open_home()
    home.search_restaurant('Test Restaurant')

    rest.add_first_item_to_cart()
    assert len(cart.get_cart_items()) > 0

    cart.proceed_to_checkout()
    checkout.select_address(0)
    # choose card and input sandbox details
    checkout.choose_card_and_pay(sandbox_card['number'], sandbox_card['exp'], sandbox_card['cvv'])
    checkout.place_order()

    order.wait_for_confirmation()
    order_id = order.get_order_id()

    # Backend verification
    resp = api_client.get(f"/orders/{order_id}")
    assert resp.status_code == 200
    body = resp.json()
    assert body.get('payment_state') in ('Paid', 'paid')

    # Check payment gateway logs - assumes test endpoint
    tx_resp = api_client.get(f"/payments?order_id={order_id}")
    assert tx_resp.status_code == 200
    txs = tx_resp.json()
    assert any(t.get('status') == 'authorized' or t.get('status') == 'success' for t in txs)
