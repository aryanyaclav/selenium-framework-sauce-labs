import pages_selectors
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utilities.driver_func_lib import DriverFuncLib
from utilities.drivermanager import DriverManager
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


class LoginPage(pages_selectors.Selectors):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver_func_lib = DriverFuncLib(self.driver)

    def enter_username(self, username):
        logging.info(f"Entering username: {username}")
        self.driver_func_lib.enter_text_textbox(self.username_textbox, username)

    def enter_password(self, password):
        logging.info(f"Entering password: {password}")
        self.driver_func_lib.enter_text_textbox(self.password_textbox, password)

    def click_login(self):
        logging.info("Clicking login button")
        self.driver_func_lib.assert_and_click(self.login_button)