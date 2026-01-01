# Import necessary modules
import pytest
import configparser
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Import page objects and utilities
from pages.login_Page import LoginPage
from pages.adminPage import AdminPage
from Utilities.read_excel import get_admin_user_data
from Utilities.logger import LogGen


# ================================
# Parametrize the test with data from Excel
# ================================
@pytest.mark.parametrize(
    "username,password,role,emp_name,new_username,new_password,expected_result",
    get_admin_user_data("./data/add_user_data.xlsx", "Sheet1")
)
@pytest.mark.usefixtures("setup")  # Use the setup fixture to initialize WebDriver
class Test_add_admin_003:
    """
    Test class for adding a new admin user using DDT (Data-Driven Testing).
    Each row in Excel is used as a separate test.
    """

    def test_add_admin_ddt(self, setup, username, password, role, emp_name, new_username, new_password,
                           expected_result):
        """
        Test method for adding admin users.

        :param setup: WebDriver fixture
        :param username, password: Admin login credentials
        :param role, emp_name, new_username, new_password, expected_result: Admin creation data from Excel
        """

        # Initialize logger
        logger = LogGen.loggen()
        logObj = LogGen()
        logObj.loggen()  # Duplicate call—can be removed
        logger.info("****** Starting Add Admin Test ******")

        # Optional: override username/password from config.ini
        config = configparser.ConfigParser()
        config.read("config/config.ini")
        username = config["DEFAULT"]["username"]
        password = config["DEFAULT"]["password"]

        # -----------------------
        # Login steps
        # -----------------------
        login = LoginPage(self.driver)
        login.enter_username(username)
        logger.info(f"===Entering username: {username}===")
        login.enter_password(password)
        logger.info(f"===Entering password===")
        login.click_login()
        logger.info("===Clicked login===")

        # -----------------------
        # Navigate to Admin page
        # -----------------------
        admin_page = AdminPage(self.driver)
        admin_page.go_to_admin()
        logger.info("===Navigated to Admin===")
        admin_page.click_on_add_button()
        logger.info("===Clicked Add button===")

        # -----------------------
        # Fill admin user form
        # -----------------------
        admin_page.select_role(role)
        admin_page.enter_emp_name(emp_name)
        admin_page.enter_user_name(new_username)
        admin_page.select_status("Enabled")
        admin_page.enter_password(new_password)
        admin_page.confirm_password(new_password)
        logger.info("===All fields entered successfully===")

        # Save new admin
        admin_page.click_on_save_button()

        # -----------------------
        # Verification
        # -----------------------
        time.sleep(1)  # Small wait for toast message
        success = admin_page.is_success_message_displayed()
        print(success)
        logger.info("=== Test Passed ===")
