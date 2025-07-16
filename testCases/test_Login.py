import pytest
from pageObjects.login_Page import LoginPage
import configparser

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login(self):
        # Load credentials from config.ini
        config = configparser.ConfigParser()
        config.read("config/config.ini")
        username = config["DEFAULT"]["username"]
        password = config["DEFAULT"]["password"]

        # Create LoginPage object
        login = LoginPage(self.driver)
        print("login succesful")

        # Perform actions
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()

        # Assertion – check if redirected to dashboard
        assert "dashboard" in self.driver.current_url.lower()
