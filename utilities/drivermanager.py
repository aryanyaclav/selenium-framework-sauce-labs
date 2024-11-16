import unittest
import logging
from selenium import webdriver
from constants import *


#define the logging format
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class DriverManager(unittest.TestCase):
    def setUp(self):
        logging.info("Setting up the driver")
        if browser == "chrome":
            self.driver = webdriver.Chrome()
            logging.info("Chrome driver created")
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            logging.error("Invalid browser type")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(url)

    def tearDown(self):
        if self.driver is not None:
            logging.info("Tearing down the driver")
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
        