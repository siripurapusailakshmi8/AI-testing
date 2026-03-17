from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Open Website (ERROR: wrong URL)
    driver.get("https://www.saucedemoo.com/")
    time.sleep(2)

    # Step 2: Login (ERROR: wrong locator ID)
    driver.find_element(By.ID, "username").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # ERROR: missing click on login button

    time.sleep(2)

    # Step 3: Add to Cart (ERROR: wrong element ID)
    driver.find_element(By.ID, "add-to-cart-backpack").click()
    print("Product added to cart")

    time.sleep(2)

    # Step 4: Go to Cart (ERROR: wrong locator type)
    driver.find_element(By.ID, "shopping_cart_link").click()

    time.sleep(2)

    # Step 5: Checkout (ERROR: wrong button ID)
    driver.find_element(By.ID, "checkot").click()

    time.sleep(2)

    # Step 6: Enter Checkout Details (ERROR: wrong field IDs)
    driver.find_element(By.ID, "firstname").send_keys("Sai")
    driver.find_element(By.ID, "lastname").send_keys("Lakshmi")
    driver.find_element(By.ID, "zipcode").send_keys("500010")

    # ERROR: missing continue button click

    time.sleep(2)

    # Step 7: Finish Order (ERROR: element not visible yet)
    driver.find_element(By.ID, "finish").click()

    time.sleep(2)

    # Step 8: Order Confirmation (ERROR: wrong class name)
    confirmation_text = driver.find_element(By.CLASS_NAME, "complete-text").text

    if "Order successful" in confirmation_text:
        print("Order placed successfully!")
    else:
        print("Order failed!")

except Exception as e:
    print("Error occurred:", e)

finally:
    driver.quit()
