import time
import pytest, configparser
from pageObjects.adminPage_Search import AdminUserSearchPage
from pageObjects.login_Page import LoginPage
from pageObjects.adminPage import AdminPage
from Utilities.logger import LogGen


@pytest.mark.usefixtures("setup")
class TestSearchUser_role():
    def test_search_by_user_role(self, setup):
        loggen_obj = LogGen.loggen()
        loggen_obj.info("****** Starting Search by Role ******")
        driver = setup
        loggen_obj.info("---- setup Initiated -----")
        config = configparser.ConfigParser()
        config.read("./config/config.ini")
        baseurl = config["DEFAULT"]["baseurl"]
        username = config["DEFAULT"]["username"]
        loggen_obj.info("---- getting Username -----")
        password = config["DEFAULT"]["password"]
        loggen_obj.info("---- getting URL -----")
        # driver.get(baseurl)

        # login
        login_obj = LoginPage(driver)
        loggen_obj.info("---- Login Page Activated -----")
        login_obj.enter_username(username)
        loggen_obj.info("---- Enter Username -----")
        login_obj.enter_password(password)
        loggen_obj.info("---- Enter Password -----")
        login_obj.click_login()
        loggen_obj.info("---- Clicked Login Button -----")
        time.sleep(2)

        # go to admin
        adminpage_obj = AdminPage(driver)
        adminpage_obj.go_to_admin()
        loggen_obj.info("---- Click on Admin -----")
        time.sleep(2)

        # search by role
        adminsearch_obj = AdminUserSearchPage(driver)
        loggen_obj.info("---- Navigate to Search Page -----")
        adminsearch_obj.select_user_role("Admin")
        loggen_obj.info("---- Paste Admin  -----")
        adminsearch_obj.click_on_search_button()
        loggen_obj.info("---- Click on Search button -----")
        time.sleep(5)
        driver.close()
        loggen_obj.info("****** Search by user role testcase Passed ******")



