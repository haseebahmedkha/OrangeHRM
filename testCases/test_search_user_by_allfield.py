from Utilities.logger import LogGen
from conftest import setup
from pageObjects.login_Page import LoginPage
from pageObjects.adminPage_Search import AdminUserSearchpage
from pageObjects.adminPage import AdminPage
import pytest,configparser
import time
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class Test_searchuser_allfield:
    def test_search_all_field(self,setup):
        driver = setup
        logger_obj = LogGen.loggen()
        login_obj = LoginPage(setup)
        admin_page_obj = AdminPage(setup)
        admin_search_obj = AdminUserSearchpage(setup)
        config = configparser.ConfigParser()
        config.read("./config/config.ini")
        username = config["DEFAULT"]["username"]
        password = config["DEFAULT"]["password"]

        logger_obj.info("============= Search By All Field Test started =======================")

        login_obj.enter_username(username)
        logger_obj.info("------------ Enter Username Successfully ---------------")
        login_obj.enter_password(password)
        logger_obj.info("------------ Enter Password Successfully ---------------")
        login_obj.click_login()
        time.sleep(4)
        logger_obj.info("------------ Click Login Button Successfully ---------------")

        admin_page_obj.go_to_admin()
        logger_obj.info("------------ Clicked Admin fro sidebar Successfully ---------------")
        time.sleep(5)

        admin_search_obj.drop_up_down_system_user()
        logger_obj.info("------------ system_user_up_down Successfully ---------------")

        admin_search_obj.enter_username("Forrest_Howe")
        logger_obj.info("------------ Put Forrest_Howe Successfully ---------------")
        admin_search_obj.select_user_role("ESS")
        logger_obj.info("------------ Select ESS Successfully ---------------")
        admin_search_obj.enter_employee_name("Forrest  Howe")
        time.sleep(4)
        logger_obj.info("------------ Put Forrest Howe Successfully ---------------")
        admin_search_obj.select_status("Enable")
        logger_obj.info("------------ Select Enable Successfully ---------------")
        admin_search_obj.click_on_search_button()
        logger_obj.info("------------ Click Search Button Successfully ---------------")
        time.sleep(6)
        url = []
        get_url = driver.current_url
        url.append(get_url)
        logger_obj.info(f"the url of current page: {url}")
        driver.close()
        logger_obj.info("============= Search By All Field Test Passed =======================")




















