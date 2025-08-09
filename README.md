This repository consists of following concepts covered in form of exercises

1. **Setting up webdriver**: using chrome
   
example:
   ```
   from selenium import webdriver
   driver = webdriver.Chrome()
   driver.get("https://example.com")
   ```

2. **Implicit and Explicit Waits**: wait for certain amount of time before searching for elements
   - implicit wait: driver.implicity_wait()
   - explicit wait: wait = WebDriverWait(driver), element = wait.until()
     
3. **Locating web elements**: different approaches to find web elements
   -  find_element_by_id
   -  find_element_by_name
   -  find_element_by_xpath
   -  find_element_by_css_selector
   -  find_element_by_class_name
   -  find_element_by_tag_name

4. **Select list elements**: selecting elements from dopdown, open list etc.
   - select_by_value
   - select_by_index
   - select_by_visible_text
