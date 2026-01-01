# Import necessary modules
import pytest
import configparser

# Import page objects and utilities
from Utilities.logger import LogGen
from pageObjects.login_Page import LoginPage
from pageObjects.dashboard_page import DashboardPage


# ================================
# Test Class for Dashboard Access
# ================================
@pytest.mark.usefixtures("setup")  # Use the Selenium WebDriver fixture
class TestDashboard_002:
    """
    Test class to validate Dashboard page access, menu items, and widgets.
    """

    @pytest.mark.smoke  # Mark this test as part of smoke suite
    @pytest.mark.regression  # Also include in regression suite
    def test_dashboard_access(self):
        """
        Test method to validate:
        1. Successful login
        2. Dashboard page URL and header
        3. Presence of left menu items
        4. Presence of key dashboard widgets
        """

        # -----------------------
        # Initialize logger
        # -----------------------
        logger = LogGen.loggen()
        logger.info("****** Test Started: Dashboard Access ******")

        # -----------------------
        # Read credentials from config.ini
        # -----------------------
        config = configparser.ConfigParser()
        config.read("./config/config.ini")
        username = config["DEFAULT"]["username"]
        password = config["DEFAULT"]["password"]

        # -----------------------
        # Perform Login
        # -----------------------
        login = LoginPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
        logger.info("Login performed successfully")

        # -----------------------
        # Dashboard validations
        # -----------------------
        dashboard = DashboardPage(self.driver)
        dashboard.wait_until_loaded()  # Wait until dashboard fully loads
        logger.info("Dashboard Page Loaded")

        # URL should contain '/dashboard'
        assert "/dashboard" in self.driver.current_url.lower(), "URL does not contain '/dashboard'"

        # Verify dashboard header text
        header = dashboard.header_text()
        logger.info(f"Dashboard Header Text: {header}")
        assert header == "Dashboard", f"Expected header 'Dashboard' but got '{header}'"

        # Verify left menu items
        menu = dashboard.visibility_menu_items()
        logger.info(f"Visible Left Menu Items: {menu}")
        must_have_menu = {"Admin", "PIM", "Leave"}
        missing_menu = must_have_menu - set(menu)
        assert not missing_menu, f"Missing Menu Items: {missing_menu}"

        # Verify dashboard widgets
        expected_widgets = ["Time at Work", "My Actions", "Quick Launch"]
        missing_widgets = dashboard.widgets_present(expected_widgets)
        assert not missing_widgets, f"Missing dashboard widgets: {missing_widgets}"
        logger.info(f"Expected Widgets: {expected_widgets} | Missing: {missing_widgets}")

        # -----------------------
        # Test completion log
        # -----------------------
        logger.info("Dashboard validations passed")
        logger.info("****** Test Ended: Dashboard Access ******")
