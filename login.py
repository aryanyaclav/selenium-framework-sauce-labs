from selenium import webdriver

driver = webdriver.Chrome()  # Make sure to have the correct driver (e.g., chromedriver)
driver.get("https://www.saucedemo.com/")
print(driver.title)
driver.quit()
