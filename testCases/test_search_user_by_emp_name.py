import time
import pytest, configparser
from pageObjects.adminPage_Search import AdminUserSearchpage
from pageObjects.login_Page import LoginPage
from pageObjects.adminPage import AdminPage
from Utilities.logger import LogGen


@pytest.mark.usefixtures("setup")
class TestSearchUser_name_employee:
    employee_name = "Linda Anderson"
    def test_search_by_employee_name(self,setup):
        driver = setup
        loggen = LogGen.loggen()
        loggen.info("============= search with Employee name Test started =======================")
        config = configparser.ConfigParser()
        config.read("./config/config.ini")
        username = config["DEFAULT"]["username"]
        loggen.info("---- getting Username -----")
        password = config["DEFAULT"]["password"]
        loggen.info("---- getting Password -----")
        loggen.info("========= Navigate to Login Page =================")
        login_obj = LoginPage(driver)
        loggen.info("---- Login Page Activated -----")
        login_obj.enter_username(username)
        loggen.info("---- Enter Username -----")
        login_obj.enter_password(password)
        loggen.info("---- Enter Password -----")
        login_obj.click_login()
        loggen.info("---- Clicked Login Button -----")
        time.sleep(6)
        loggen.info("========= Navigate to Admin Page =================")
        admin_obj = AdminPage(setup)
        admin_obj.go_to_admin()
        loggen.info("--------------- Clicked on Admin ----------------------")
        time.sleep(5)
        admin_search_obj = AdminUserSearchpage(setup)
        loggen.info("========= Navigate to Admin User Search Page =================")
        admin_search_obj.enter_employee_name(self.employee_name)
        loggen.info("----------- Enter Employee Name --------------------------------")
        admin_search_obj.click_on_search_button()
        assert not admin_search_obj.get_search_result() == "Linda Anderson", "Employee not found in search results"
        loggen.info("============= search with Employee name Test Passed =======================")




