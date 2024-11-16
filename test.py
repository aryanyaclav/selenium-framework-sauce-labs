from selenium import webdriver

driver = webdriver.Chrome()  # Make sure to have the correct driver (e.g., chromedriver)
# driver.get("https://www.google.com")
# print(driver.title)
# driver.quit()

print(driver.capabilities['chrome']['chromedriverVersion'])

