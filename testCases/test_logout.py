import time
from itertools import dropwhile
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.login_Page import LoginPage
import configparser
from Utilities.logger import LogGen
from Utilities.read_excel import get_login_data
from pageObjects.logout_page import LogoutPage


@pytest.mark.usefixtures("setup")
class TestLogout():

    def test_logout(self,setup):
        URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        # for Creating log `object
        logger = LogGen.loggen()
        logger.info("****** Logout Test has been Started ******")
        config = configparser.ConfigParser()
        config.read("config/config.ini")
        username = config["DEFAULT"]["username"]
        password = config["DEFAULT"]["password"]

        login_obj = LoginPage(setup)
        logger.info("===Navigating to the login page===")
        login_obj.enter_username(username)
        logger.info("===Entering username===")
        time.sleep(5)
        login_obj.enter_password(password)
        logger.info("===Entering Password===")
        time.sleep(5)
        login_obj.click_login()
        logger.info("===clicked login===")
        # sleep for 5 seconds
        time.sleep(5)
        logout_obj = LogoutPage(setup)
        logger.info("===click on Dropdown===")
        time.sleep(3)
        logout_obj.click_on_logout()
        logger.info("===click on logout Successfully===")
        time.sleep(4)


        if URL in setup.current_url:
            assert True
            logger.info("===Logout testcase passed===")
        else:
            logger.error("===Logout testcase failed===")
            assert False










