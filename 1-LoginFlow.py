# Steps:
# 1. Open the website
# 2. Enter username and Password
# 3. Click login
# 4. Verify successful login by checking the page title or URL
# 5. Take a screenshot after login
# 6. close the browser


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

assert "inventory" in driver.current_url, "Login failed"

driver.save_screenshot("login_success.png")

driver.quit()

