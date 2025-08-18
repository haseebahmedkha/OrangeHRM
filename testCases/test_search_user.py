import time
import pytest, configparser
from pageObjects.adminPage_Search import AdminUserSearchpage
from pageObjects.login_Page import LoginPage
from pageObjects.adminPage import AdminPage
from Utilities.logger import LogGen


@pytest.mark.usefixtures("setup")
class TestSearchUser:
    def test_search_by_username(self, setup):
        driver = setup
        loggen_obj = LogGen.loggen()
        loggen_obj.info("****** Starting Search Admin Test ******")

        # get username and password
        config = configparser.ConfigParser()
        config.read("./config/config.ini")
        username = config["DEFAULT"]["username"]
        password = config["DEFAULT"]["password"]

        # login
        login_obj = LoginPage(driver)
        login_obj.enter_username(username)
        login_obj.enter_password(password)
        login_obj.click_login()
        loggen_obj.info("------ succesfully Login  --------")

        # go to admin
        adminpage_obj = AdminPage(driver)
        adminpage_obj.go_to_admin()
        time.sleep(3)

        # search
        adminsearch_obj = AdminUserSearchpage(driver)
        adminsearch_obj.enter_username("admin")
        adminsearch_obj.click_on_search_button()
        time.sleep(2)

        result = adminsearch_obj.get_search_result()
        assert not any("Admin" in row.text for row in result), \
            "Username 'Admin' not found in search results"

        loggen_obj.info("****** Search Admin Test Passed ******")

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
        driver.get(baseurl)

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
        adminsearch_obj = AdminUserSearchpage(driver)
        loggen_obj.info("---- Navigate to Search Page -----")
        adminsearch_obj.select_user_role("Admin")
        loggen_obj.info("---- Paste Admin  -----")
        adminsearch_obj.click_on_search_button()
        loggen_obj.info("---- Click on Search button -----")
        time.sleep(2)
        loggen_obj.info("****** Search by user role testcase Passed ******")

# the above two cases is executing perfectly when run seperately but when i execute as a whole its throws timeoutException Error.