"""
Pages package for Page Object Model.
"""

# Expose page classes at package level
from .base_page import BasePage
from .login_page import LoginPage
from .home_page import HomePage
from .restaurant_page import RestaurantPage
from .cart_page import CartPage
from .checkout_page import CheckoutPage
from .order_page import OrderPage
from .tracking_page import TrackingPage
from .payment_page import PaymentPage

__all__ = [
    "BasePage",
    "LoginPage",
    "HomePage",
    "RestaurantPage",
    "CartPage",
    "CheckoutPage",
    "OrderPage",
    "TrackingPage",
    "PaymentPage",
]

# Note: individual page implementations are in separate files
"}