from selenium.webdriver.common.by import By
import pages_selectors.login_page_selectors

class HomePageSelectors(pages_selectors.login_page_selectors.LoginPage_selectors):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.logout_button = (By.ID, "logout_sidebar_link")
        self.error_message = (By.XPATH, "//h3[@data-test='error']")
        self.navbar_button = (By.ID, "react-burger-menu-btn")
        self.add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.filter_buttn = (By.CLASS_NAME, "product_sort_container")
        self.cart_buttton = (By.ID, "shopping_cart_container")
        self.remove_from_cart_button = (By.ID, "remove-sauce-labs-backpack")
        self.allItemsButton = (By.ID, "inventory_sidebar_link")
        self.aboutButton = (By.ID, "about_sidebar_link")
        self.logoutButton = (By.ID, "logout_sidebar_link")
        self.resetButton = (By.ID, "reset_sidebar_link")
