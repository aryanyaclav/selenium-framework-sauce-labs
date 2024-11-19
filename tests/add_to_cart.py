from utilities.drivermanager import DriverManager
from constants import *
import pages.login_page
import pages.home_page

class TestAddToCart(DriverManager):
    def test_addToCart(self):
        login_page = pages.login_page.LoginPage(self.driver, self.logger)
        login_page.enter_username(username)    
        login_page.enter_password(password)
        login_page.click_login()
        #wait for page to load
        self.driver.implicitly_wait(5)
        home_page = pages.home_page.HomePage(self.driver, self.logger)
        home_page.add_to_cart()