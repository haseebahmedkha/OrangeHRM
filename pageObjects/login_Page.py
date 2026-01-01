from selenium.webdriver.support import expected_conditions as EC  # Import expected conditions for explicit waits
from selenium.webdriver.common.by import By  # Import By class to locate elements
from selenium.webdriver.support.wait import WebDriverWait  # Import WebDriverWait for explicit waiting
from pageObjects.basePage import BasePage  # Import the BasePage class (assuming this contains common functionality for all pages)


class LoginPage(BasePage):
    # Locators for the Login page elements
    # Previously using strings directly; now using tuples with By strategy
    # name = "//input[@placeholder='Username']"
    # password = "//input[@placeholder='Password']"
    # login_button = "//button[@type='submit']"

    # Define element locators as tuples (By.<strategy>, locator_value)
    name = (By.XPATH, "//input[@placeholder='Username']")  # Username input field
    password = (By.XPATH, "//input[@placeholder='Password']")  # Password input field
    login_button = (By.XPATH, "//button[@type='submit']")  # Login button

    def __init__(self, driver):
        self.driver = driver  # Assign the Selenium WebDriver instance to the page
        self.wait = WebDriverWait(driver, 10)  # Create an explicit wait object with a 10-second timeout

    def enter_username(self, username):
        # Wait until the username input field is visible on the page
        self.wait.until(EC.visibility_of_element_located(self.name))
        # Find the username input field and enter the provided username
        self.driver.find_element(*self.name).send_keys(username)

    def enter_password(self, password):
        # Wait until the password input field is visible on the page
        self.wait.until(EC.visibility_of_element_located(self.password))
        # Find the password input field and enter the provided password
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        # Wait until the login button is visible on the page
        self.wait.until(EC.visibility_of_element_located(self.login_button))
        # Find the login button and perform a click action
        self.driver.find_element(*self.login_button).click()
