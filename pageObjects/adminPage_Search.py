import time
from gc import enable
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Utilities.logger import LogGen

class AdminUserSearchPage:
    # Locators
    search_user_name = (By.XPATH,"//label[text()='Username']/../following-sibling::div/input")
    role_dropdown = (By.XPATH, "//label[text()='User Role']/../following-sibling::div//div[contains(@class,'oxd-select-text-input')]")
    search_button = (By.XPATH,"//button[normalize-space()='Search']")
    reset_button = (By.XPATH,"//button[normalize-space()='Reset']")
    result_table = (By.XPATH, "//div[@role='table']")
    result_rows = (By.XPATH, "//div[@role='rowgroup']/div[@role='row']")
    employee_name_field = (By.XPATH,"//input[@placeholder='Type for hints...']")
    system_user_element = (By.XPATH, "//div[@class='--toggle']//button[@type='button']")
    select_element_status = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]")
    enable_select_element = (By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[2]")

    # Delete Locators
    user_checkbox = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row'][1]//input[@type='checkbox']")
    delete_button = (By.XPATH, "//button[@class='oxd-icon-button oxd-table-cell-action-space'][1]")
    confirm_delete = (By.XPATH, "//button[normalize-space()='Yes, Delete']")


    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)


    def enter_username(self,put_username):
        field = self.wait.until(EC.presence_of_element_located(self.search_user_name))
        field.clear()
        field.send_keys(put_username)

    def select_user_role(self,role_text):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.role_dropdown)
        )
        dropdown.click()
        time.sleep(2)
        # Click option inside dropdown
        option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='option']/span[text()='{role_text}']"))
        )
        option.click()

    def enter_employee_name(self,enter_employee_name):
        emp_field = self.wait.until(EC.presence_of_element_located(self.employee_name_field))
        emp_field.clear()
        emp_field.send_keys(enter_employee_name)
        time.sleep(2)
        return emp_field.send_keys()

    def select_status(self,dropdown_value):
        # Click option inside dropdown
        select_option = self.wait.until(
            EC.element_to_be_clickable(self.select_element_status)
        )
        select_option.click()
        time.sleep(2)
        enable_option = self.wait.until(EC.element_to_be_clickable(self.enable_select_element))
        enable_option.click()

    def drop_up_down_system_user(self):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.system_user_element)
        )
        dropdown.click()
        time.sleep(2)
        dropdown.click()

    def click_on_search_button(self):
        self.wait.until(EC.element_to_be_clickable(self.search_button)).click()

    def click_reset_button(self):
        self.wait.until(EC.element_to_be_clickable(self.reset_button)).click()

    def select_first_user_checkbox(self):
        checkbox = self.wait.until(EC.element_to_be_clickable(self.user_checkbox))
        checkbox.click()

    def click_delete_button(self):
        delete_btn = self.wait.until(EC.element_to_be_clickable(self.delete_button))
        delete_btn.click()

    def click_confirm_deletion(self):
        confirm_btn = self.wait.until(EC.element_to_be_clickable(self.confirm_delete))
        confirm_btn.click()

    def get_search_result(self):
        self.wait.until(EC.presence_of_element_located(self.result_rows))
        return self.driver.find_elements(*self.result_rows)

