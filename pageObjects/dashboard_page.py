from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    header = (By.XPATH,"//h6[normalize-space()='Dashboard']")
    menu_items = (By.CSS_SELECTOR, "aside .oxd-main-menu-item--name")
    widget_title = (By.CSS_SELECTOR,
                     "div.orangehrm-dashboard-widget div.oxd-sheet--title, div.orangehrm-dashboard-widget p.oxd-text--p")


    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def wait_until_loaded(self):
        self.wait.until(EC.url_contains("/dashboard"))
        self.wait.until(EC.visibility_of_element_located(self.header))

    def header_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.header)).get_attribute("textContent").strip()

    def visibility_menu_items(self):
        self.wait.until(EC.presence_of_all_elements_located(self.menu_items))
        els = self.driver.find_elements(*self.menu_items)
        return [e.get_attribute("textContent").strip() for e in els if e.get_attribute("textContent")]

    def widget_titles(self):
        self.wait.until(EC.presence_of_all_elements_located(self.widget_title))
        els = self.driver.find_elements(*self.widget_title)
        return [e.get_attribute("textContent").strip() for e in els if e.get_attribute("textContent")]

    def widgets_present(self, expected_titles):
        titles = [t.lower() for t in self.widget_titles()]
        missing = [t for t in expected_titles if t.lower() not in titles]
        return missing  # empty list means all found
