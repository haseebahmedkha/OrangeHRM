# ================================
# Imports
# ================================
import time
import pytest
import configparser

# Page Objects and Utilities
from pages.login_Page import LoginPage
from pages.adminPage import AdminPage
from pages.adminPage_Search import AdminUserSearchPage
from Utilities.logger import LogGen


# ================================
# Test Class: Search Admin Users by Role
# ================================
@pytest.mark.usefixtures("setup")  # Use setup fixture for WebDriver
class TestSearchUser_role:
    """
    Test class to validate searching for admin users by User Role.
    """

    def test_search_by_user_role(self, setup):
        """
        Test steps:
        1. Login using credentials from config.ini
        2. Navigate to Admin page
        3. Select a User Role from the dropdown
        4. Click Search
        5. Validate results
        """
        driver = setup
        logger = LogGen.loggen()
        logger.info("****** Starting Search by Role Test ******")

        # -----------------------
        # Load credentials from config.ini
        # -----------------------
        config = configparser.ConfigParser()
        config.read("./config/config.ini")
        baseurl = config["DEFAULT"]["baseurl"]
        username = config["DEFAULT"]["username"]
        password = config["DEFAULT"]["password"]

        logger.info("---- Loaded configuration values -----")
        # driver.get(baseurl)  # Optional if fixture already navigates to base URL

        # -----------------------
        # Perform Login
        # -----------------------
        login_obj = LoginPage(driver)
        logger.info("---- Login Page Activated -----")
        login_obj.enter_username(username)
        logger.info("---- Entered Username -----")
        login_obj.enter_password(password)
        logger.info("---- Entered Password -----")
        login_obj.click_login()
        logger.info("---- Clicked Login Button -----")
        time.sleep(2)  # Replace with explicit wait for dashboard

        # -----------------------
        # Navigate to Admin Page
        # -----------------------
        adminpage_obj = AdminPage(driver)
        adminpage_obj.go_to_admin()
        logger.info("---- Navigated to Admin Page -----")
        time.sleep(2)  # Replace with explicit wait for admin page elements

        # -----------------------
        # Search users by Role
        # -----------------------
        adminsearch_obj = AdminUserSearchPage(driver)
        logger.info("---- Navigate to Admin User Search Page -----")
        adminsearch_obj.select_user_role("Admin")  # Select role 'Admin'
        logger.info("---- Selected Role: Admin  -----")
        adminsearch_obj.click_on_search_button()
        logger.info("---- Clicked on Search Button -----")
        time.sleep(5)  # Wait for search results (replace with explicit wait)

        # -----------------------
        # Validate search results
        # -----------------------
        results = adminsearch_obj.get_search_result()  # Returns list of WebElements

        # Ensure at least one user with role 'Admin' exists
        assert any("Admin" in row.text for row in results), "No users with role 'Admin' found in search results"

        # -----------------------
        # Tear down
        # -----------------------
        driver.close()
        logger.info("****** Search by User Role Test Passed ******")
