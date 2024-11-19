import unittest
import logging
from selenium import webdriver
from utilities import logging_config
from constants import *


#define the logging format
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class DriverManager(unittest.TestCase):
    def setUp(self):
        #logging part
        testname = self._testMethodName
        self.logger = logging_config.setup_logger(testname)

        #web driver setup
        self.logger.info("Setting up the driver")
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            self.driver = webdriver.Chrome(options=options)
            self.logger.info("Chrome driver created")
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.logger.error("Invalid browser type")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(url)

    def tearDown(self):
        if self.driver is not None:
            self.logger.info("Tearing down the driver")
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
        