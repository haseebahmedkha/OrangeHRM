import time

import pytest
from pageObjects.login_Page import LoginPage
import configparser
from Utilities.logger import LogGen
from Utilities.read_excel import get_login_data

login_data = get_login_data("./testData/test_data.xlsx","Sheet1")




@pytest.mark.usefixtures("setup")
class TestLogin_001:
    def test_valid_login(self):
        # Load credentials from config.ini
        logger = LogGen.loggen()
        logger.info("****** Test Started: Valid Login ******")

        config = configparser.ConfigParser()
        config.read("config/config.ini")
        username = config["DEFAULT"]["username"]
        password = config["DEFAULT"]["password"]

        # Create LoginPage object
        login = LoginPage(self.driver)
        logger.info("===Navigating to the login page===")
        print("login succesful")

        # Perform actions
        login.enter_username(username)
        logger.info("===Entering username===")
        login.enter_password(password)
        logger.info("===Entering Password===")
        login.click_login()
        logger.info("===clicked login===")

        if "dashboard" in self.driver.current_url.lower():
            logger.info("===Login successful and testcase passed")
            assert True
        else:
            logger.error("===Login Failed, testcase failed")
            assert False
        logger.info("Loggen test cases ended")

        # Assertion – check if redirected to dashboard
        # assert "dashboard" in self.driver.current_url.lower()


    # login testcase with DDT
    @pytest.mark.parametrize("username,password,expected_result",login_data)
    def test_login_ddt(self,setup,username,password,expected_result):
        logger = LogGen.loggen()
        driver = setup
        logger.info("Setup Initialized")
        login = LoginPage(driver)
        logger.info("login ddt testcase started")
        login.enter_username(username)
        logger.info("Enter username")
        login.enter_password(password)
        logger.info("Enter password")
        login.click_login()
        logger.info("click Login button Successfully")

        if expected_result == "Pass":
            assert "dashboard" in driver.current_url.lower()
        else:
            assert "dashboard" not in driver.current_url.lower()





