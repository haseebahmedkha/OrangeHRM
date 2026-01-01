from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LogoutPage(BasePage):

    # Locators
    user_dropdown = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    logout_link = (By.XPATH, "//a[text()='Logout']")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    # ------- Not working Because Select works with HTML select tag but in Orange Hrm uses li ---------
    # def select_visible_by_text(self,locator,text):
    #     element_selected = self.driver.find_element(locator).click()
    #     select = Select(element_selected)
    #     select.select_by_visible_text(text)
    #
    # def select_visible_by_value(self,locator,value):
    #     select = Select(self.driver.find_element(locator))
    #     select.select_by_value(value)

    # click on logout
    def click_on_logout(self):
        self.wait.until(EC.visibility_of_element_located(self.user_dropdown)).click()
        self.wait.until(EC.visibility_of_element_located(self.logout_link)).click()




