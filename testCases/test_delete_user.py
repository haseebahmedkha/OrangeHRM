from Utilities.logger import LogGen
from pageObjects.adminPage import AdminPage
from pageObjects.adminPage_Search import AdminUserSearchpage
import pytest,configparser,time
from pageObjects.login_Page import LoginPage
from conftest import setup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class TestSearchUserDelete:
    #Locators
    sure_text = (By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-text--card-title']")
    assure_text = (By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-text--card-body']")

    def test_search_by_delete(self,setup):
        driver = setup
        logger_obj = LogGen.loggen()
        login_obj = LoginPage(setup)
        admin_page_obj = AdminPage(setup)
        admin_search_obj = AdminUserSearchpage(setup)
        config = configparser.ConfigParser()
        config.read("./config/config.ini")
        username = config["DEFAULT"]["username"]
        password = config["DEFAULT"]["password"]

        logger_obj.info("============= Delete User TestCase started =======================")

        login_obj.enter_username(username)
        logger_obj.info("------------ Enter Username Successfully ---------------")
        login_obj.enter_password(password)
        logger_obj.info("------------ Enter Password Successfully ---------------")
        login_obj.click_login()
        time.sleep(4)
        logger_obj.info("------------ Click Login Button Successfully ---------------")

        admin_page_obj.go_to_admin()
        logger_obj.info("------------ Clicked Admin from sidebar Successfully ---------------")
        time.sleep(5)

        admin_search_obj.enter_username("")
        logger_obj.info("------------ Put User Data Successfully ---------------")
        admin_search_obj.select_user_role("ESS")
        logger_obj.info("------------ Select ESS Successfully ---------------")
        admin_search_obj.click_on_search_button()
        logger_obj.info("------------ Click Search Button Successfully ---------------")
        time.sleep(6)
        admin_search_obj.click_delete_button()
        logger_obj.info("------------ Click Delete Button Successfully ---------------")
        time.sleep(2)

        sure_text_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(self.sure_text)
        )
        actual_text = sure_text_element.text
        if actual_text.strip() == "Are you Sure?":
            admin_search_obj.click_confirm_deletion()
            logger_obj.info("------------ Click Confirm Button Successfully ---------------")
            time.sleep(3)
            driver.close()
            logger_obj.info("============= Delete User TestCase Passed =======================")
        else:
            assert False


