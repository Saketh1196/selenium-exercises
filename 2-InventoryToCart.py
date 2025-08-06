from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# launching webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# logging in to the website
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

# adding items to cart
driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()

# verifying whether correct items are there in the cart
driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

time.sleep(2)
cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
cart_item_names = [item.text for item in cart_items]

assert "Sauce Labs Backpack" in cart_item_names, "Backpack not found in cart"
assert "Sauce Labs Bike Light" in cart_item_names, "Bike Light not found in cart"

# taking the screenshot
driver.save_screenshot("Cart_items.png")

driver.quit()
