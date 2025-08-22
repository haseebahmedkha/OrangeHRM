import time
import pytest, configparser
from pageObjects.adminPage_Search import AdminUserSearchpage
from pageObjects.login_Page import LoginPage
from pageObjects.adminPage import AdminPage
from Utilities.logger import LogGen


@pytest.mark.usefixtures("setup")
class TestSearchUser_name:
    def test_search_by_username(self, setup):
        driver = setup
        loggen_obj = LogGen.loggen()
        loggen_obj.info("****** Starting Search By Username Test ******")
        # get username and password
        config = configparser.ConfigParser()
        config.read("./config/config.ini")
        username = config["DEFAULT"]["username"]
        password = config["DEFAULT"]["password"]

        # login
        login_obj = LoginPage(driver)
        login_obj.enter_username(username)
        loggen_obj.info("--------- Enter Username --------------")
        login_obj.enter_password(password)
        loggen_obj.info("--------- Enter Password --------------")
        login_obj.click_login()
        loggen_obj.info("------ succesfully Login  --------")

        # go to admin
        adminpage_obj = AdminPage(driver)
        adminpage_obj.go_to_admin()
        loggen_obj.info("--------- click on Admin Button --------------")
        time.sleep(3)

        # search
        adminsearch_obj = AdminUserSearchpage(driver)
        loggen_obj.info("--------- Admin Page Now --------------")
        adminsearch_obj.enter_username("admin")
        loggen_obj.info("--------- Pasting Admin on Field --------------")
        adminsearch_obj.click_on_search_button()
        loggen_obj.info("--------- Clicking search button --------------")
        time.sleep(2)

        result = adminsearch_obj.get_search_result()
        assert not any("Admin" in row.text for row in result), \
            "Username 'Admin' not found in search results"
        loggen_obj.info("****** Search By Name Test Passed ******")
        driver.close()





