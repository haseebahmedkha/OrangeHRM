from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    name = "username"
    password = "password"
    login_button = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def enter_username(self, username):
        wait = WebDriverWait(self.driver, 10)  # Wait for a maximum of 10 seconds
        username_field = wait.until(EC.presence_of_element_located((By.NAME, self.name)))
        self.driver.find_element(By.NAME,self.name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME,self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.login_button).click()


