# ================================
# Imports
# ================================
import time
import pytest
import configparser

# Page Objects and Utilities
from pageObjects.login_Page import LoginPage
from pageObjects.adminPage import AdminPage
from pageObjects.adminPage_Search import AdminUserSearchPage
from Utilities.logger import LogGen


# ================================
# Test Class: Search Admin User by Employee Name
# ================================
@pytest.mark.usefixtures("setup")  # Use setup fixture for WebDriver
class TestSearchUser_name_employee:
    """
    Test class to validate searching for an admin user by Employee Name.
    """
    employee_name = "Linda Anderson"

    def test_search_by_employee_name(self, setup):
        """
        Test steps:
        1. Login using credentials from config.ini
        2. Navigate to Admin page
        3. Search using the Employee Name field
        4. Validate search results
        """
        driver = setup
        logger = LogGen.loggen()

        logger.info("============= Search by Employee Name Test started =======================")

        # -----------------------
        # Load credentials from config.ini
        # -----------------------
        config = configparser.ConfigParser()
        config.read("./config/config.ini")
        username = config["DEFAULT"]["username"]
        password = config["DEFAULT"]["password"]

        logger.info("---- Retrieved login credentials -----")

        # -----------------------
        # Perform Login
        # -----------------------
        login_obj = LoginPage(driver)
        logger.info("========= Navigating to Login Page =================")
        login_obj.enter_username(username)
        logger.info("---- Entered Username -----")
        login_obj.enter_password(password)
        logger.info("---- Entered Password -----")
        login_obj.click_login()
        logger.info("---- Clicked Login Button -----")
        time.sleep(6)  # Wait for dashboard to load (replace with explicit wait)

        # -----------------------
        # Navigate to Admin Page
        # -----------------------
        admin_obj = AdminPage(driver)
        logger.info("========= Navigate to Admin Page =================")
        admin_obj.go_to_admin()
        logger.info("--------------- Clicked on Admin ----------------------")
        time.sleep(5)  # Wait for Admin page to load

        # -----------------------
        # Search by Employee Name
        # -----------------------
        admin_search_obj = AdminUserSearchPage(driver)
        logger.info("========= Navigate to Admin User Search Page =================")
        admin_search_obj.enter_employee_name(self.employee_name)
        logger.info(f"----------- Entered Employee Name: {self.employee_name} --------------------------------")
        admin_search_obj.click_on_search_button()
        logger.info("----------- Clicked Search Button --------------------------------")
        time.sleep(3)  # Wait for search results
