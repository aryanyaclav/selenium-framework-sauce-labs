from selenium.webdriver.common.by import By

class LoginPage_selectors():
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox = (By.ID, "user-name")
        self.password_textbox = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.XPATH, "//h3[@data-test='error']")