from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://trytestingthis.netlify.app/")

select_element = driver.find_element(By.ID,"option")
dropdown = Select(select_element)
dropdown.select_by_value("option 2")

multiple_select = driver.find_element(By.ID,"owc")
dropdown1 = Select(multiple_select)
dropdown1.select_by_index(3)

time.sleep(5)
driver.save_screenshot("drop_down.png")
print("Dropdown Successfull")

driver.quit()

