import pytest, configparser
from Utilities.logger import LogGen
from pageObjects.login_Page import LoginPage
from pageObjects.dashboard_page import DashboardPage

@pytest.mark.usefixtures("setup")
class TestDashboard_002:

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_dashboard_access(self):
        logger = LogGen.loggen()
        logger.info("****** Test Started: Dashboard Access ******")

        # credentials from confi.ini file
        config = configparser.ConfigParser()
        config.read("./config/config.ini")
        username = config["DEFAULT"]["username"]
        password = config["DEFAULT"]["password"]

        # create object for loginpage
        login = LoginPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()

        # dashboard Validation
        dashboard = DashboardPage(self.driver)
        dashboard.wait_until_loaded()
        logger.info("Dashboard Page Loaded")

        # url contains dashbaoard
        assert "/dashboard" in self.driver.current_url.lower(), "URL does not contains /dashboard"

        # Header Text
        header = dashboard.header_text()
        logger.info(f"Dashboard Header Text: {header}")
        assert header == "Dashboard", f"Expected header 'Dashboard' but got '{header}'"

        # Key menu items and widgets present
        menu = dashboard.visibility_menu_items()
        logger.info(f"visible Left Menu Items: {menu}")

        must_have_menu = {"Admin","PIM","Leave"}
        assert must_have_menu.issubset(set(menu)), f"Missing Menu Items from {must_have_menu - set(menu)}"

        expected_widgets = ["Time at Work", "My Actions", "Quick Launch"]
        missing_widgets = dashboard.widgets_present(expected_widgets)
        assert not missing_widgets, f"Missing dashbaord widgets: {missing_widgets}"
        logger.info(f"Expected Widgets: {expected_widgets + missing_widgets}")

        logger.info("Dashboard validations passed")
        logger.info("****** Test Ended: Dashboard Access ******")








