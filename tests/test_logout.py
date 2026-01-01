# ================================
# Imports
# ================================
import time
import pytest
import configparser
from selenium.webdriver.support.wait import WebDriverWait

# Page Objects and Utilities
from pages.login_Page import LoginPage
from pages.logout_page import LogoutPage
from Utilities.logger import LogGen
from Utilities.read_excel import get_login_data


# ================================
# Test Class: Logout Functionality
# ================================
@pytest.mark.usefixtures("setup")  # Use setup fixture to initialize WebDriver
class TestLogout:
    """
    Test class to validate logout functionality.
    """

    def test_logout(self, setup):
        """
        Validates that a user can logout successfully and is redirected to the login page.
        """

        # Expected login URL after logout
        URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

        # -----------------------
        # Initialize logger
        # -----------------------
        logger = LogGen.loggen()
        logger.info("****** Logout Test has been Started ******")

        # -----------------------
        # Load credentials from config.ini
        # -----------------------
        config = configparser.ConfigParser()
        config.read("config/config.ini")
        username = config["DEFAULT"]["username"]
        password = config["DEFAULT"]["password"]

        # -----------------------
        # Perform Login
        # -----------------------
        login_obj = LoginPage(setup)
        logger.info("===Navigating to the login page===")
        login_obj.enter_username(username)
        logger.info("===Entering username===")
        time.sleep(5)  # Replace with explicit wait for username field if possible

        login_obj.enter_password(password)
        logger.info("===Entering password===")
        time.sleep(5)  # Replace with explicit wait for password field if possible

        login_obj.click_login()
        logger.info("===Clicked login===")
        time.sleep(5)  # Wait for dashboard to load (replace with explicit wait)

        # -----------------------
        # Perform Logout
        # -----------------------
        logout_obj = LogoutPage(setup)
        logger.info("===Click on user dropdown===")
        time.sleep(3)  # Wait for dropdown to be clickable (use explicit wait instead)

        logout_obj.click_on_logout()
        logger.info("===Clicked logout successfully===")
        time.sleep(4)  # Wait for redirect to login page

        # -----------------------
        # Validation: Check if redirected to login page
        # -----------------------
        if URL in setup.current_url:
            assert True
            logger.info("===Logout test case passed===")
        else:
            logger.error("===Logout test case failed===")
            assert False
