import pytest, configparser
import time
from pageObjects.adminPage_Search import AdminUserSearchpage
from pageObjects.login_Page import LoginPage
from pageObjects.adminPage import AdminPage
from pageObjects.dashboard_page import DashboardPage
from Utilities.logger import LogGen

@pytest.mark.usefixtures("setup")
class TestSearchUser_Enabale_disable_dropdown:
    def test_search_by_enable_disable(self,setup):
        driver = setup
        logs_obj = LogGen.loggen()
        config = configparser.ConfigParser()
        config.read("./config/config.ini")
        username = config["DEFAULT"]["username"]
        password = config["DEFAULT"]["password"]
        logs_obj.info("============= search with Enable/Disable Dropdown Test started =======================")

        login_obj = LoginPage(driver)
        logs_obj.info("------------ created Login Page Object successfully ---------------")
        login_obj.enter_username(username)
        logs_obj.info("------------ Enter Username Successfully ---------------")
        login_obj.enter_password(password)
        logs_obj.info("------------ Enter Password Successfully ---------------")
        login_obj.click_login()
        time.sleep(3)
        logs_obj.info("------------ Click Login Button Successfully ---------------")

        admin_page_obj = AdminPage(driver)
        logs_obj.info("------------ created Admin Page Object successfully ---------------")
        admin_page_obj.go_to_admin()
        logs_obj.info("------------ Clicked Admin fro sidebar Successfully ---------------")
        time.sleep(4)

        admin_user_search_obj = AdminUserSearchpage(driver)
        logs_obj.info("------------ created Admin Page Object successfully ---------------")
        admin_user_search_obj.select_status("Enable")
        logs_obj.info("------------ systemUser minimize/maximize successfully ---------------")
        time.sleep(2)
        logs_obj.info("------------ Click on Enable successfully ---------------")
        admin_user_search_obj.click_on_search_button()
        time.sleep(3)
        logs_obj.info("------------ Clicked on Search Button successfully ---------------")
        assert not admin_user_search_obj.get_search_result() == "Enable", "Users with selected status not found in results"
        driver.close()
        logs_obj.info("============= search Enable/Disable Test Passed =======================")






