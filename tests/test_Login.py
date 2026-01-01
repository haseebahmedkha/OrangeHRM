# ================================
# Imports
# ================================
import time
import pytest
import configparser
from selenium.webdriver.support.wait import WebDriverWait

# Page Objects and Utilities
from pages.login_Page import LoginPage
from Utilities.logger import LogGen
from Utilities.read_excel import get_login_data


# ================================
# Test Class for Login Functionality
# ================================
@pytest.mark.usefixtures("setup")  # Use setup fixture to initialize WebDriver
class TestLogin_001:
    """
    Test class to validate login functionality.
    Includes:
    1. Sanity test with valid credentials
    2. Data-driven tests (DDT) for multiple credentials from Excel
    """

    # -----------------------
    # Sanity Test: Valid Login
    # -----------------------
    @pytest.mark.sanity
    def test_valid_login(self, setup):
        """
        Validates successful login using credentials from config.ini
        """
        logger = LogGen.loggen()  # Initialize logger
        logger.info("****** Test Started: Valid Login ******")

        # Load credentials from config.ini
        config = configparser.ConfigParser()
        config.read("config/config.ini")
        username = config["DEFAULT"]["username"]
        password = config["DEFAULT"]["password"]

        # Create LoginPage object
        login = LoginPage(setup)
        logger.info("===Navigating to the login page===")

        # Perform login actions with slight delays
        # (Delays can be replaced by explicit waits for elements)
        time.sleep(5)
        login.enter_username(username)
        logger.info("===Entering username===")

        time.sleep(5)
        login.enter_password(password)
        logger.info("===Entering password===")

        time.sleep(5)
        login.click_login()
        logger.info("===Clicked login===")

        # Verify login success by checking if URL contains "dashboard"
        if "dashboard" in setup.current_url.lower():
            time.sleep(6)
            logger.info("===Login successful, test case passed===")
            assert True
        else:
            logger.error("===Login failed, test case failed===")
            assert False

        logger.info("****** Login test case ended ******")


    # -----------------------
    # Data-Driven Test (DDT) using Excel
    # -----------------------
    login_data = get_login_data("./data/test_data.xlsx", "Sheet1")

    @pytest.mark.regression
    @pytest.mark.parametrize("username,password,expected_result", login_data)
    def test_login_ddt(self, setup, username, password, expected_result):
        """
        Performs login with multiple sets of credentials from Excel.
        Validates expected result: Pass or Fail.
        """
        logger = LogGen.loggen()  # Initialize logger
        driver = setup
        logger.info("Setup initialized for DDT login test")

        # Create LoginPage object
        login = LoginPage(driver)
        logger.info("Login DDT test case started")

        # Enter username and password
        login.enter_username(username)
        logger.info(f"Entering username: {username}")

        login.enter_password(password)
        logger.info(f"Entering password")

        login.click_login()
        logger.info("Clicked Login button successfully")

        # Validate login result based on expected_result
        if expected_result == "Pass":
            assert "dashboard" in driver.current_url.lower(), "Expected login to succeed but failed"
        else:
            assert "dashboard" not in driver.current_url.lower(), "Expected login to fail but succeeded"
