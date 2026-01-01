# ================================
# Imports
# ================================
from Utilities.logger import LogGen
from pageObjects.adminPage import AdminPage
from pageObjects.adminPage_Search import AdminUserSearchPage
from pageObjects.login_Page import LoginPage
from conftest import setup

import pytest
import configparser
import time

# Selenium imports
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ================================
# Test Class for Searching and Deleting Admin User
# ================================
@pytest.mark.usefixtures("setup")  # Use the setup fixture for WebDriver
class TestSearchUserDelete:
    """
    This test class handles searching for a user and deleting it from the Admin page.
    """

    # -----------------------
    # Locators for deletion confirmation pop-up
    # -----------------------
    sure_text = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--card-title']")
    assure_text = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--card-body']")

    # ================================
    # Test Method: Search and Delete User
    # ================================
    def test_search_by_delete(self, setup):
        """
        Test to search for an admin user and delete it.
        Verifies that the deletion confirmation popup appears before confirming.
        """

        driver = setup  # WebDriver instance
        logger_obj = LogGen.loggen()  # Initialize logger

        # Create page objects
        login_obj = LoginPage(driver)
        admin_page_obj = AdminPage(driver)
        admin_search_obj = AdminUserSearchPage(driver)

        # Load login credentials from config.ini
        config = configparser.ConfigParser()
        config.read("./config/config.ini")
        username = config["DEFAULT"]["username"]
        password = config["DEFAULT"]["password"]

        logger_obj.info("============= Delete User TestCase started =======================")

        # -----------------------
        # Perform Login
        # -----------------------
        login_obj.enter_username(username)
        logger_obj.info("------------ Enter Username Successfully ---------------")
        login_obj.enter_password(password)
        logger_obj.info("------------ Enter Password Successfully ---------------")
        login_obj.click_login()
        time.sleep(4)  # Wait for dashboard to load
        logger_obj.info("------------ Click Login Button Successfully ---------------")

        # -----------------------
        # Navigate to Admin Page
        # -----------------------
        admin_page_obj.go_to_admin()
        logger_obj.info("------------ Clicked Admin from sidebar Successfully ---------------")
        time.sleep(5)  # Wait for Admin page to fully load

        # -----------------------
        # Search User to Delete
        # -----------------------
        admin_search_obj.enter_username("")  # Empty string to search all users
        logger_obj.info("------------ Put User Data Successfully ---------------")
        admin_search_obj.select_user_role("ESS")  # Select role filter
        logger_obj.info("------------ Select ESS Successfully ---------------")
        admin_search_obj.click_on_search_button()
        logger_obj.info("------------ Click Search Button Successfully ---------------")
        time.sleep(6)  # Wait for search results to populate

        # -----------------------
        # Delete User
        # -----------------------
        admin_search_obj.click_delete_button()
        logger_obj.info("------------ Click Delete Button Successfully ---------------")
        time.sleep(2)

        # Wait for confirmation popup to appear
        sure_text_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(self.sure_text)
        )

        # Validate popup text before confirming deletion
        actual_text = sure_text_element.text
        if actual_text.strip() == "Are you Sure?":
            admin_search_obj.click_confirm_deletion()
            logger_obj.info("------------ Click Confirm Button Successfully ---------------")
            time.sleep(3)

            # Close the browser after test
            driver.close()
            logger_obj.info("============= Delete User TestCase Passed =======================")
            assert True
        else:
            logger_obj.error("Delete confirmation popup not displayed as expected")
            assert False
