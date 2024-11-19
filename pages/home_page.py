import pages_selectors
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utilities.driver_func_lib import DriverFuncLib
from utilities.drivermanager import DriverManager
import logging

#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class HomePage(pages_selectors.Selectors):
    def __init__(self, driver, logger):
        super().__init__(driver)
        self.driver = driver
        self.logger = logger
        self.driver_func_lib = DriverFuncLib(self.driver, self.logger)

    def add_to_cart(self):
        self.driver_func_lib.assert_and_click(self.add_to_cart_button)
        self.logger.info("Item added to cart")
        self.driver_func_lib.is_elelement_visible(self.remove_from_cart_button)
        self.logger.info("Remove button is visible")
    
    def logout(self):
        self.driver_func_lib.assert_and_click(self.navbar_button)
        self.logger.info("Opened Navbar")
        self.driver_func_lib.assert_and_click(self.logout_button)
        self.logger.info("Logged out")
        self.driver_func_lib.is_elelement_visible(self.login_button)
        self.logger.info("Login button is visible")


    