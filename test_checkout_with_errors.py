import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_checkout_happy_path(driver):
    wait = WebDriverWait(driver, 10)

    # Step 1: Open Website
    driver.get("https://www.saucedemo.com/")

    # Step 2: Login
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Step 3: Add product to cart
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()

    # Step 4: Go to cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Step 5: Checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # Step 6: Enter details
    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Sai")
    driver.find_element(By.ID, "last-name").send_keys("Lakshmi")
    driver.find_element(By.ID, "postal-code").send_keys("500010")
    driver.find_element(By.ID, "continue").click()

    # Step 7: Finish order
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

    # Step 8: Verify confirmation
    confirmation_text = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    ).text

    assert "THANK YOU FOR YOUR ORDER" in confirmation_text
