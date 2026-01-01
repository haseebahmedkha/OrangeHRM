# ================================
# Imports
# ================================
import pytest
import configparser
import time

# Page Objects and Utilities
from pageObjects.login_Page import LoginPage
from pageObjects.adminPage import AdminPage
from pageObjects.adminPage_Search import AdminUserSearchPage
from Utilities.logger import LogGen


# ================================
# Test Class: Search Admin Users by Status (Enable/Disable)
# ================================
@pytest.mark.usefixtures("setup")  # Use setup fixture for WebDriver
class TestSearchUser_Enable_disable_dropdown:
    """
    Test class to validate searching for admin users using the Status dropdown (Enable/Disable)
    """

    def test_search_by_enable_disable(self, setup):
        """
        Test steps:
        1. Login with credentials from config.ini
        2. Navigate to Admin page
        3. Select 'Enable' status from dropdown
        4. Perform search
        5. Validate results
        """
        driver = setup
        logger = LogGen.loggen()

        # -----------------------
        # Load credentials from config.ini
        # -----------------------
        config = configparser.ConfigParser()
        config.read("./config/config.ini")
        username = config["DEFAULT"]["username"]
        password = config["DEFAULT"]["password"]

        logger.info("============= Search with Enable/Disable Dropdown Test started =======================")

        # -----------------------
        # Login to application
        # -----------------------
        login_obj = LoginPage(driver)
        logger.info("------------ Created Login Page object ---------------")
        login_obj.enter_username(username)
        logger.info("------------ Entered Username Successfully ---------------")
        login_obj.enter_password(password)
        logger.info("------------ Entered Password Successfully ---------------")
        login_obj.click_login()
        time.sleep(3)  # Wait for dashboard (replace with explicit wait)
        logger.info("------------ Clicked Login Button Successfully ---------------")

        # -----------------------
        # Navigate to Admin Page
        # -----------------------
        admin_page_obj = AdminPage(driver)
        logger.info("------------ Created Admin Page object ---------------")
        admin_page_obj.go_to_admin()
        logger.info("------------ Clicked Admin from sidebar Successfully ---------------")
        time.sleep(4)

        # -----------------------
        # Search users by Status dropdown
        # -----------------------
        admin_user_search_obj = AdminUserSearchPage(driver)
        logger.info("------------ Created Admin User Search Page object ---------------")

        admin_user_search_obj.select_status("Enable")  # Select 'Enable' from dropdown
        logger.info("------------ Selected 'Enable' from Status dropdown successfully ---------------")
        time.sleep(2)

        admin_user_search_obj.click_on_search_button()  # Click Search
        time.sleep(3)
        logger.info("------------ Clicked Search Button successfully ---------------")

        # -----------------------
        # Validate search results
        # -----------------------
        results = admin_user_search_obj.get_search_result()  # Returns list of WebElements

        # Check if at least one result has 'Enable' status
        assert any("Enable" in row.text for row in results), "Users with selected status 'Enable' not found in results"

        # Close browser (optional if fixture handles teardown)
        driver.close()
        logger.info("============= Search Enable/Disable Test Passed =======================")
