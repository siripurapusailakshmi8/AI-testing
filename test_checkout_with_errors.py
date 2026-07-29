"""Checkout functionality tests."""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.test_data import TestData, BrowserConfig
from utils.logger import get_logger

logger = get_logger(__name__)


class TestCheckout:
    """Test suite for Checkout functionality."""

    @pytest.mark.smoke
    def test_checkout_happy_path(self, driver):
        """Test complete checkout flow.
        
        Steps:
            1. Open website
            2. Login with valid credentials
            3. Add product to cart
            4. Go to cart
            5. Proceed to checkout
            6. Enter shipping details
            7. Finish order
            8. Verify confirmation message
        """
        logger.info("Starting test_checkout_happy_path")
        wait = WebDriverWait(driver, BrowserConfig.wait_time)

        try:
            # Step 1: Open Website
            logger.info("Step 1: Opening website")
            driver.get("https://www.saucedemo.com/")

            # Step 2: Login
            logger.info("Step 2: Logging in")
            wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(
                TestData.username
            )
            driver.find_element(By.ID, "password").send_keys(TestData.password)
            driver.find_element(By.ID, "login-button").click()

            # Step 3: Add product to cart
            logger.info("Step 3: Adding product to cart")
            wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()

            # Step 4: Go to cart
            logger.info("Step 4: Going to cart")
            driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

            # Step 5: Checkout
            logger.info("Step 5: Starting checkout")
            wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

            # Step 6: Enter details
            logger.info("Step 6: Entering checkout details")
            wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys(
                TestData.first_name
            )
            driver.find_element(By.ID, "last-name").send_keys(TestData.last_name)
            driver.find_element(By.ID, "postal-code").send_keys(TestData.postal_code)
            driver.find_element(By.ID, "continue").click()

            # Step 7: Finish order
            logger.info("Step 7: Finishing order")
            wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

            # Step 8: Verify confirmation
            logger.info("Step 8: Verifying confirmation")
            confirmation_text = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
            ).text

            assert "THANK YOU FOR YOUR ORDER" in confirmation_text, "Confirmation message not found"
            logger.info("Test passed: Checkout successful")

        except Exception as e:
            logger.error(f"Test failed with error: {e}")
            raise

    @pytest.mark.regression
    def test_checkout_invalid_postal_code(self, driver):
        """Test checkout with invalid postal code.
        
        Expected: Error message for invalid postal code
        """
        logger.info("Starting test_checkout_invalid_postal_code")
        wait = WebDriverWait(driver, BrowserConfig.wait_time)

        try:
            # Login
            logger.info("Logging in")
            driver.get("https://www.saucedemo.com/")
            wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(
                TestData.username
            )
            driver.find_element(By.ID, "password").send_keys(TestData.password)
            driver.find_element(By.ID, "login-button").click()

            # Add product and proceed to checkout
            logger.info("Adding product and proceeding to checkout")
            wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
            driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
            wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

            # Enter invalid postal code
            logger.info("Entering invalid postal code")
            wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys(
                TestData.first_name
            )
            driver.find_element(By.ID, "last-name").send_keys(TestData.last_name)
            driver.find_element(By.ID, "postal-code").send_keys("INVALID")
            driver.find_element(By.ID, "continue").click()

            # Check for error message
            logger.info("Checking for error message")
            error_element = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "error-message"))
            )
            assert error_element is not None, "Error message not found"
            logger.info("Test passed: Invalid postal code validation working")

        except Exception as e:
            logger.error(f"Test failed with error: {e}")
            raise
