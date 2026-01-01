from selenium.webdriver.support.select import Select  # Import Select class for handling dropdowns (HTML <select> elements)
from selenium.webdriver.support.wait import WebDriverWait  # Import WebDriverWait for explicit waits
from pageObjects.basePage import BasePage  # Import BasePage for common page functionality
from selenium.webdriver.common.by import By  # Import By class for locating elements
from selenium.webdriver.support import expected_conditions as EC  # Import expected conditions for explicit waits


class LogoutPage(BasePage):

    # Locators for the Logout page elements
    user_dropdown = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")  # Dropdown element for user menu
    logout_link = (By.XPATH, "//a[text()='Logout']")  # Logout link inside the dropdown menu

    def __init__(self,driver):
        self.driver = driver  # Assign the Selenium WebDriver instance to this page
        self.wait = WebDriverWait(driver,10)  # Create an explicit wait object with a 10-second timeout

    # ------- Not working Because Select works with HTML <select> tag but in Orange HRM uses <li> ---------
    # def select_visible_by_text(self,locator,text):
    #     element_selected = self.driver.find_element(locator).click()
    #     select = Select(element_selected)
    #     select.select_by_visible_text(text)
    #
    # def select_visible_by_value(self,locator,value):
    #     select = Select(self.driver.find_element(locator))
    #     select.select_by_value(value)
    # Above methods are commented because OrangeHRM uses <li> for dropdown items instead of <select>
    # Selenium's Select class only works with <select> elements, so custom click logic is needed

    # Click on logout link
    def click_on_logout(self):
        # Wait until the user dropdown is visible, then click to expand the menu
        self.wait.until(EC.visibility_of_element_located(self.user_dropdown)).click()
        # Wait until the logout link is visible, then click to log out
        self.wait.until(EC.visibility_of_element_located(self.logout_link)).click()
