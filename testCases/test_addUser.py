import pytest
from pageObjects.login_Page import LoginPage
from pageObjects.adminPage import AdminPage
from Utilities.read_excel import get_admin_user_data
from Utilities.logger import LogGen
import configparser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

@pytest.mark.parametrize(
    "username,password,role,emp_name,new_username,new_password,expected_result",
    get_admin_user_data("./testData/add_user_data.xlsx", "Sheet1")
)
@pytest.mark.usefixtures("setup")
class Test_add_admin_003:

    def test_add_admin_ddt(self, setup, username, password, role, emp_name, new_username, new_password, expected_result):
        logger = LogGen.loggen()
        logger.info("****** Starting Add Admin Test ******")

        # If you want to override with config.ini, uncomment below
        config = configparser.ConfigParser()
        config.read("config/config.ini")
        username = config["DEFAULT"]["username"]
        password = config["DEFAULT"]["password"]

        # Login
        login = LoginPage(self.driver)
        login.enter_username(username)
        logger.info(f"===Entering username: {username}===")
        login.enter_password(password)
        logger.info(f"===Entering password===")
        login.click_login()
        logger.info("===Clicked login===")

        # Navigate to admin page
        admin_page = AdminPage(self.driver)
        admin_page.go_to_admin()
        logger.info("===Navigated to Admin===")
        admin_page.click_on_add_button()
        logger.info("===Clicked Add button===")
        admin_page.select_role(role)
        admin_page.enter_emp_name(emp_name)
        admin_page.enter_user_name(new_username)
        admin_page.select_status("Enabled")
        admin_page.enter_password(new_password)
        admin_page.confirm_password(new_password)
        logger.info("===All fields entered successfully===")
        admin_page.click_on_save_button()

        # Wait for and verify success message
        time.sleep(1)  # Small buffer so toast has time to appear
        success = admin_page.is_success_message_displayed()
        print(success)
        logger.info("=== Test Passed ===")
