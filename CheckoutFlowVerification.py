from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# launching webdriver
driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.saucedemo.com/")

# logging in to the website
driver.find_element(By.ID,"user-name").send_keys("visual_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

# adding items to cart
driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()

# verifying whether correct items are there in the cart
driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

wait = WebDriverWait(driver, 10)
# going to checkout and filling details
driver.find_element(By.ID,"checkout").click()
first_name = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
first_name.send_keys("Test")

first_name = wait.until(EC.visibility_of_element_located((By.ID, "last-name")))
first_name.send_keys("User")

first_name = wait.until(EC.visibility_of_element_located((By.ID, "postal-code")))
first_name.send_keys("12345")


driver.find_element(By.ID,"continue").click()

# verifying items in the cart
time.sleep(2)
cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
cart_item_names = [item.text for item in cart_items]

assert "Sauce Labs Backpack" in cart_item_names, "Backpack not found in cart"
assert "Sauce Labs Bike Light" in cart_item_names, "Bike Light not found in cart"
assert "Item total" in driver.find_element(By.CLASS_NAME,"summary_subtotal_label").text, "Item total not found"

driver.save_screenshot("Checkout_items.png")

driver.quit()