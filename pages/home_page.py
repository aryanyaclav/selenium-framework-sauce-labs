import pages_selectors.home_page_selectors
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utilities.driver_func_lib import DriverFuncLib
from utilities.drivermanager import DriverManager
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class HomePage(pages_selectors.home_page_selectors.HomePageSelectors):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver_func_lib = DriverFuncLib(self.driver)

    def add_to_cart(self):
        self.driver_func_lib.assert_and_click(self.add_to_cart_button)
        logging.info("Item added to cart")
        self.driver_func_lib.is_elelement_visible(self.remove_from_cart_button)
        logging.info("Remove button is visible")
    
    def logout(self):
        self.driver_func_lib.assert_and_click(self.navbar_button)
        logging.info("Opened Navbar")
        self.driver_func_lib.assert_and_click(self.logout_button)
        logging.info("Logged out")
        self.driver_func_lib.is_elelement_visible(self.login_button)
        logging.info("Login button is visible")


    