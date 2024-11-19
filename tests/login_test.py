from utilities.drivermanager import DriverManager
from constants import *
import pages.login_page

class TestLogin(DriverManager):
    def test_login(self):
        login_page = pages.login_page.LoginPage(self.driver, self.logger)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()
        login_page.driver_func_lib.assert_element_not_present(login_page.error_message)
