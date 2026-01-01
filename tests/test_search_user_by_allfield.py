# ================================
# Imports
# ================================
import time
import pytest
import configparser
from selenium.webdriver.common.by import By

# Page Objects and Utilities
from Utilities.logger import LogGen
from pages.login_Page import LoginPage
from pages.adminPage import AdminPage
from pages.adminPage_Search import AdminUserSearchPage
from conftest import setup


# ================================
# Test Class: Search Admin User by All Fields
# ================================
@pytest.mark.usefixtures("setup")  # Use setup fixture for WebDriver
class TestSearchUserAllField:
    """
    Test class to validate searching for an admin user using all search fields.
    """

    def test_search_all_field(self, setup):
        """
        Test steps:
        1. Login using credentials from config.ini
        2. Navigate to Admin page
        3. Perform search using all available filters:
           - System User dropdown
           - Username
           - User Role
           - Employee Name
           - Status
        4. Verify the current URL after search
        """

        driver = setup

        # -----------------------
        # Initialize logger and page objects
        # -----------------------
        logger = LogGen.loggen()
        login_obj = LoginPage(driver)
        admin_page_obj = AdminPage(driver)
        admin_search_obj = AdminUserSearchPage(driver)

        # Load login credentials from config.ini
        config = configparser.ConfigParser()
        config.read("./config/config.ini")
        username = config["DEFAULT"]["username"]
        password = config["DEFAULT"]["password"]

        logger.info("============= Search By All Field Test started =======================")

        # -----------------------
        # Perform Login
        # -----------------------
        login_obj.enter_username(username)
        logger.info("------------ Enter Username Successfully ---------------")
        login_obj.enter_password(password)
        logger.info("------------ Enter Password Successfully ---------------")
        login_obj.click_login()
        time.sleep(4)  # Wait for dashboard to load (replace with explicit wait)
        logger.info("------------ Click Login Button Successfully ---------------")

        # -----------------------
        # Navigate to Admin Page
        # -----------------------
        admin_page_obj.go_to_admin()
        logger.info("------------ Clicked Admin from sidebar Successfully ---------------")
        time.sleep(5)  # Wait for Admin page to load

        # -----------------------
        # Fill all search fields
        # -----------------------
        admin_search_obj.drop_up_down_system_user()
        logger.info("------------ System User dropdown interacted successfully ---------------")

        admin_search_obj.enter_username("Forrest_Howe")
        logger.info("------------ Entered username: Forrest_Howe ---------------")

        admin_search_obj.select_user_role("ESS")
        logger.info("------------ Selected User Role: ESS ---------------")

        admin_search_obj.enter_employee_name("Forrest Howe")
        time.sleep(4)  # Wait for autocomplete or validation
        logger.info("------------ Entered Employee Name: Forrest Howe ---------------")

        admin_search_obj.select_status("Enable")
        logger.info("------------ Selected Status: Enable ---------------")

        admin_search_obj.click_on_search_button()
        logger.info("------------ Clicked Search Button Successfully ---------------")
        time.sleep(6)  # Wait for search results to load

        # ------
