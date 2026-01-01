
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    driver = webdriver.Chrome

    def find(self,locator):
        return self.driver.find_element(locator)

    def clear_element(self,locator):
        self.driver.find_element(locator).clear()

    def send_values(self,locator,value):
        self.clear_element(locator)
        self.driver.find_element(locator).send_keys(value)

    def click_on_element(self,locator):
        self.driver.find_element(locator).click()

    def get_text(self,locator):
        return self.driver.find_element(locator).text








