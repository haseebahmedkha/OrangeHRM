from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# class variables
class AdminPage:
    admin_menu = "//span[text()='Admin']"
    add_button = "//button[normalize-space()='Add']"
    role_dropdown = "//label[text()='User Role']/following::div[1]//select"
    emp_name_input = "//input[@placeholder='Type for hints...']"
    user_input = "//label[text()='Username']/following::input[1]"
    status_dropdown = "//label[text()='Status']/following::div[1]//select"
    pass_input = "//label[text()='Password']/following::input[1]"
    confirm_password_input = "//label[text()='Confirm Password']/following::input[1]"
    save_button = "//button[normalize-space()='Save']"
    success_message = "//div[contains(@class,'oxd-toast') and contains(text(),'Success')]"

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def go_to_admin(self):
        admin_element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.admin_menu))
        )
        admin_element.click()

    def click_on_add_button(self):
        admin_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.add_button))
                                       )
        admin_button.click()


    def select_role(self,role):
        # Click dropdown
        dropdown = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[text()='User Role']/following::div[@class='oxd-select-wrapper'][1]"))
        )
        dropdown.click()

        # Click the role option
        option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='option']/span[text()='{role}']"))
        )
        option.click()

    def enter_emp_name(self,emp_name):
        field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.emp_name_input))
        )
        field.clear()
        field.send_keys(emp_name)

        # Wait for suggestion dropdown and click first match
        suggestion = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[@role='listbox']//span[contains(text(),'{emp_name.split()[0]}')]"))
        )
        suggestion.click()

    def enter_user_name(self,user_name):
        field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.user_input))
        )
        field.clear()
        field.send_keys(user_name)

    def select_status(self,status):
        # Click dropdown
        dropdown = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[text()='Status']/following::div[@class='oxd-select-wrapper'][1]"))
        )
        dropdown.click()

        # Click the status option
        option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='option']/span[text()='{status}']"))
        )
        option.click()

    def enter_password(self,password):
        field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.pass_input))
        )
        field.clear()
        field.send_keys(password)

    def confirm_password(self,confirm_password):
        field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.confirm_password_input))
        )
        field.clear()
        field.send_keys(confirm_password)

    def click_on_save_button(self):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.save_button))
        ).click()

    def is_success_message_displayed(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.success_message))
            )
            return True
        except:
            return False








