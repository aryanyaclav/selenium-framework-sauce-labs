import logging
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class DriverFuncLib():
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        logging.info(f"Waiting for element: {locator}")
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    def assert_and_click(self, locator):
        try:
            self.wait_for_element(locator)
            ele = self.driver.find_element(*locator)
            ele.click()
            return True
        except NoSuchElementException:
            logging.error(f"Element not found: {locator}")
            return False
    
    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            logging.info(f"Element found: {locator}")
            return True
        except NoSuchElementException:
            logging.error(f"Element not found: {locator}")
            return False
        
    def assert_element_present(self, locator):
        logging.info(f"Asserting element: {locator}")
        assert self.is_element_present(locator), f"Element not found: {locator}"

    def assert_element_not_present(self, locator):
        logging.info(f"Asserting element not present: {locator}")
        assert not self.is_element_present(locator), f"Element found: {locator}"

    def wait_for_element_present(self, locator, timeout=10):
        logging.info(f"Waiting for element: {locator}")
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(By.XPATH,locator))

    def is_elelement_visible(self, locator):
        try:
            self.driver.find_element(*locator).is_displayed()
            logging.info(f"Element found: {locator}")
            return True
        except NoSuchElementException:
            logging.error(f"Element not found: {locator}")
            return False
        
    def assert_elelment_visibility(self, locator, is_visible = True):
        logging.info(f"Asserting element visibility: {locator}")
        assert is_visible == self.is_elelement_visible(locator), "Element visibility does not match"

    def enter_text_textbox(self, locator, text):
        logging.info(f"Entering text: {text} into element: {locator}")
        ele = self.driver.find_element(*locator)
        try:
            logging.info("Clearing existing text")
            ele.clear()
            ele.send_keys(text)
            logging.info("Text entered successfully")
            return True
        except NoSuchElementException:
            logging.error(f"Element not found: {locator}")
            return False
        