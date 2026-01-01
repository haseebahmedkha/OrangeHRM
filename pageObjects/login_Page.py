from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.basePage import BasePage


class LoginPage(BasePage):
    # Locators
    # name = "//input[@placeholder='Username']"
    # password = "//input[@placeholder='Password']"
    # login_button = "//button[@type='submit']"

    name = (By.XPATH, "//input[@placeholder='Username']")
    password = (By.XPATH, "//input[@placeholder='Password']")
    login_button = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        # wait = WebDriverWait(self.driver, 10)  # Wait for a maximum of 10 seconds
        self.wait.until(EC.visibility_of_element_located(self.name))
        self.driver.find_element(*self.name).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password))
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.wait.until(EC.visibility_of_element_located(self.login_button))
        self.driver.find_element(*self.login_button).click()


