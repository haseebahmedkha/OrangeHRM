# ================================
# Imports
# ================================
import time
import pytest
import configparser

# Page Objects and Utilities
from pages.adminPage_Search import AdminUserSearchPage
from pages.login_Page import LoginPage
from pages.adminPage import AdminPage
from Utilities.logger import LogGen


# ================================
# Test Class: Search Admin User by Username
# ================================
@pytest.mark.usefixtures("setup")  # Use setup fixture for WebDriver
class TestSearchUser_name:
    """
    Test class to validate searching for an admin user by username.
    """

    def test_search_by_username(self, setup):
        """
        Test steps:
        1. Login using valid credentials from config.ini
        2. Navigate to Admin page
        3. Search for a specific username
        4. Verify search results
        """

        driver = setup
        logger = LogGen.loggen()
        logger.info("****** Starting Search By Username Test ******")

        # -----------------------
        # Load credentials from config.ini
        # -----------------------
        config = configparser.ConfigParser()
        config.read("./config/config.ini")
        username = config["DEFAULT"]["username"]
        password = config["DEFAULT"]["password"]

        # -----------------------
        # Perform Login
        # -----------------------
        login_obj = LoginPage(driver)
        login_obj.enter_username(username)
        logger.info("--------- Entered Username --------------")
        login_obj.enter_password(password)
        logger.info("--------- Entered Password --------------")
        login_obj.click_login()
        logger.info("------ Successfully Logged In  --------")
        time.sleep(3)  # Wait for dashboard to load (replace with explicit wait)

        # -----------------------
        # Navigate to Admin Page
        # -----------------------
        adminpage_obj = AdminPage(driver)
        adminpage_obj.go_to_admin()
        logger.info("--------- Clicked Admin Button --------------")
        time.sleep(3)  # Wait for Admin page to load

        # -----------------------
        # Perform User Search
        # -----------------------
        adminsearch_obj = AdminUserSearchPage(driver)
        logger.info("--------- Admin Page Loaded --------------")
        adminsearch_obj.enter_username("admin")  # Search for 'admin' username
        logger.info("--------- Entered 'admin' in search field --------------")
        adminsearch_obj.click_on_search_button()
        logger.info("--------- Clicked Search Button --------------")
        time.sleep(2)  # Wait for search results

        # -----------------------
        # Validate Search Results
        # -----------------------
        result = adminsearch_obj.get_search_result()  # Returns list of WebElements

        # Ensure 'Admin' username is present in results
        assert any("Admin" in row.text for row in result), \
            "Username 'Admin' not found in search results"

        logger.info("****** Search By Name Test Passed ******")

        # Close browser (optional: could be handled by fixture teardown)
        driver.close()
