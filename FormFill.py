from selenium import webdriver
from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# launching the website
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")
driver.implicitly_wait(30)

# filling the practice form
driver.find_element(By.ID,"firstName").send_keys("Test")
driver.find_element(By.ID,"lastName").send_keys("User")
driver.find_element(By.ID,"userEmail").send_keys("abc@gmail.com")
driver.execute_script("window.scrollBy(0, 500);")
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-2']").click()
driver.find_element(By.ID,"userNumber").send_keys("9999999876")
driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']").click()

driver.find_element(By.ID,"submit").click()

assert "Thanks for submitting the form" in driver.find_element(By.ID, "example-modal-sizes-title-lg").text, "Not found"

driver.save_screenshot("filled_form.png")

print("Test pass")