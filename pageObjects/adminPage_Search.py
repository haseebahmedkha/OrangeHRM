from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminUserSearchpage:
    # Locators
    search_user_name = (By.XPATH,"//label[text()='Username']/../following-sibling::div/input")
    search_button = (By.XPATH,"//button[normalize-space()='Search']")
    reset_button = (By.XPATH,"//button[normalize-space()='Reset']")
    result_table = (By.XPATH, "//div[@role='table']")
    result_rows = (By.XPATH, "//div[@role='rowgroup']/div[@role='row']")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)


    def enter_username(self,put_username):
        field = self.wait.until(EC.presence_of_element_located(self.search_user_name))
        field.clear()
        field.send_keys(put_username)

    def click_on_search_button(self):
        self.wait.until(EC.element_to_be_clickable(self.search_button)).click()

    def click_reset_button(self):
        self.wait.until(EC.element_to_be_clickable(self.reset_button)).click()

    def get_search_result(self):
        self.wait.until(EC.presence_of_element_located(self.result_rows))
        return self.driver.find_elements(*self.result_rows)

