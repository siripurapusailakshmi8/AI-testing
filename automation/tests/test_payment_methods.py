import os
import time
from pom.pages.login_page import LoginPage
from pom.pages.home_page import HomePage
from pom.pages.restaurant_page import RestaurantPage
from pom.pages.cart_page import CartPage
from pom.pages.checkout_page import CheckoutPage

BASE_URL = os.getenv('BASE_URL', 'https://example-app-url')
TEST_USER_EMAIL = os.getenv('TEST_USER_EMAIL', 'testuser@example.com')
TEST_USER_PASSWORD = os.getenv('TEST_USER_PASSWORD', 'Password123')


def place_order_with_payment(driver, payment_method):
    login = LoginPage(driver)
    home = HomePage(driver)
    restaurant = RestaurantPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.go_to_login(BASE_URL)
    login.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)

    home.open(BASE_URL)
    home.open_first_restaurant()
    restaurant.add_first_n_items(1)
    restaurant.go_to_cart()
    cart.proceed_to_checkout()
    checkout.enter_address("123 Test St")
    assert checkout.select_payment_method(payment_method)
    checkout.pay()
    time.sleep(2)


def test_card_payment_sandbox(driver):
    place_order_with_payment(driver, "card")


def test_upi_payment_sandbox(driver):
    place_order_with_payment(driver, "upi")


def test_wallet_payment_sandbox(driver):
    place_order_with_payment(driver, "wallet")
