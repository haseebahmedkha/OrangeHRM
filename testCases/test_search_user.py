import time

import pytest,configparser
from pageObjects.adminPage_Search import AdminUserSearchpage
from pageObjects.login_Page import LoginPage
from pageObjects.adminPage import AdminPage
from Utilities.logger import LogGen

@pytest.mark.usefixtures("setup")
class TestSearchUser:
    def test_search_by_username(self,setup):

        # create LogGen Object for creating Logs
        loggen_obj = LogGen.loggen()
        loggen_obj.info("****** Starting Search Admin Test ******")


        # get username and password
        loggen_obj.info("------ getting username and password --------")
        config = configparser.ConfigParser()
        config.read("./config/config.ini")
        username = config["DEFAULT"]["username"]
        password = config["DEFAULT"]["password"]
        loggen_obj.info("------ successfully getting username and password --------")

        # create Login object for login page
        loggen_obj.info("------ getting Login page Properties and Methods --------")
        login_obj = LoginPage(self.driver)
        login_obj.enter_username(username)
        loggen_obj.info("------ Enter Username --------")
        login_obj.enter_password(password)
        loggen_obj.info("------ Enter Password --------")
        login_obj.click_login()
        loggen_obj.info("------ succesfully Login  --------")


        # Create adminpageSearch Object for getting methods for testing
        adminpage_obj = AdminPage(self.driver)
        adminpage_obj.go_to_admin()
        loggen_obj.info("------ succesfully click on Admin Button  --------")
        time.sleep(5)

        loggen_obj.info("------ succesfully on search page --------")
        adminsearch_obj = AdminUserSearchpage(self.driver)
        adminsearch_obj.enter_username("admin")
        loggen_obj.info("------ succesfully paste Admin on search field --------")
        time.sleep(4)
        adminsearch_obj.click_on_search_button()
        loggen_obj.info("------ succesfully Clicked on search Button --------")
        time.sleep(4)
        result = adminsearch_obj.get_search_result()
        assert not any("Admin" in row.text for row in result), "Username 'Admin' not found in search results"
        loggen_obj.info("****** Starting Search Admin Test Passed ******")


