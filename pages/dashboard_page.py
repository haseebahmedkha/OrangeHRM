from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    """
    Page Object Model class for OrangeHRM Dashboard page.

    This class contains:
    - Dashboard page locators
    - Methods to validate dashboard load
    - Methods to read menu items and dashboard widgets

    It helps keep dashboard-related logic separate from test cases.
    """

    # Locator for the Dashboard page header text
    header = (By.XPATH, "//h6[normalize-space()='Dashboard']")

    # Locator for all left-side menu items visible on dashboard
    menu_items = (By.CSS_SELECTOR, "aside .oxd-main-menu-item--name")

    # Locator for dashboard widget titles (cards shown on dashboard)
    widget_title = (
        By.CSS_SELECTOR,
        "div.orangehrm-dashboard-widget div.oxd-sheet--title, "
        "div.orangehrm-dashboard-widget p.oxd-text--p"
    )

    def __init__(self, driver):
        """
        Constructor to initialize driver and explicit wait.

        :param driver: WebDriver instance passed from test or fixture
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def wait_until_loaded(self):
        """
        Waits until the Dashboard page is fully loaded.

        Validation includes:
        - URL contains '/dashboard'
        - Dashboard header is visible

        This ensures that all dashboard elements are ready
        before interacting with them.
        """
        self.wait.until(EC.url_contains("/dashboard"))
        self.wait.until(EC.visibility_of_element_located(self.header))

    def header_text(self):
        """
        Fetches and returns the dashboard header text.

        :return: Cleaned header text as string
        """
        return (
            self.wait
            .until(EC.visibility_of_element_located(self.header))
            .get_attribute("textContent")
            .strip()
        )

    def visibility_menu_items(self):
        """
        Retrieves all visible menu item names from the left menu panel.

        This method:
        - Waits until all menu items are present
        - Extracts visible text from each item
        - Returns a list of menu item names

        :return: List of menu names displayed on dashboard
        """
        self.wait.until(EC.presence_of_all_elements_located(self.menu_items))
        els = self.driver.find_elements(*self.menu_items)
        return [
            e.get_attribute("textContent").strip()
            for e in els
            if e.get_attribute("textContent")
        ]

    def widget_titles(self):
        """
        Retrieves all dashboard widget titles.

        Useful for:
        - Validating dashboard UI
        - Ensuring expected widgets are present after login

        :return: List of widget title strings
        """
        self.wait.until(EC.presence_of_all_elements_located(self.widget_title))
        els = self.driver.find_elements(*self.widget_title)
        return [
            e.get_attribute("textContent").strip()
            for e in els
            if e.get_attribute("textContent")
        ]

    def widgets_present(self, expected_titles):
        """
        Validates whether expected dashboard widgets are present.

        This method:
        - Compares expected widget names with actual widget titles
        - Returns missing widget names (if any)

        :param expected_titles: List of expected widget titles
        :return: List of missing widgets (empty list means success)
        """
        titles = [t.lower() for t in self.widget_titles()]
        missing = [t for t in expected_titles if t.lower() not in titles]
        return missing  # Empty list means all widgets are present
