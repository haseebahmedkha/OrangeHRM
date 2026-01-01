import time
from gc import enable
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Utilities.logger import LogGen


class AdminUserSearchPage:
    """
    Page Object class for Admin → User Search functionality
    This class contains all locators and actions related to searching,
    filtering, and deleting system users from the Admin page.
    """

    # =======================
    # Locator Definitions
    # =======================

    # Username search input field
    search_user_name = (By.XPATH, "//label[text()='Username']/../following-sibling::div/input")

    # User Role dropdown (Admin / ESS)
    role_dropdown = (
        By.XPATH,
        "//label[text()='User Role']/../following-sibling::div//div[contains(@class,'oxd-select-text-input')]"
    )

    # Search and Reset buttons
    search_button = (By.XPATH, "//button[normalize-space()='Search']")
    reset_button = (By.XPATH, "//button[normalize-space()='Reset']")

    # Search result table and rows
    result_table = (By.XPATH, "//div[@role='table']")
    result_rows = (By.XPATH, "//div[@role='rowgroup']/div[@role='row']")

    # Employee name auto-suggestion input field
    employee_name_field = (By.XPATH, "//input[@placeholder='Type for hints...']")

    # System Users dropdown toggle
    system_user_element = (By.XPATH, "//div[@class='--toggle']//button[@type='button']")

    # Status dropdown and enable option
    select_element_status = (
        By.XPATH,
        "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]"
    )
    enable_select_element = (
        By.XPATH,
        "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[2]"
    )

    # =======================
    # Delete User Locators
    # =======================

    # Checkbox of first user in result table
    user_checkbox = (
        By.XPATH,
        "//div[@class='oxd-table-body']//div[@role='row'][1]//input[@type='checkbox']"
    )

    # Delete button for selected user
    delete_button = (
        By.XPATH,
        "//button[@class='oxd-icon-button oxd-table-cell-action-space'][1]"
    )

    # Confirmation button for delete popup
    confirm_delete = (By.XPATH, "//button[normalize-space()='Yes, Delete']")

    # =======================
    # Constructor
    # =======================

    def __init__(self, driver):
        """
        Initializes the AdminUserSearchPage with WebDriver instance
        and explicit wait.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # =======================
    # Page Actions
    # =======================

    def enter_username(self, put_username):
        """
        Enters the username into the search input field.
        """
        field = self.wait.until(EC.presence_of_element_located(self.search_user_name))
        field.clear()
        field.send_keys(put_username)

    def select_user_role(self, role_text):
        """
        Selects a user role from the User Role dropdown.
        Example values: 'Admin', 'ESS'
        """
        dropdown = self.wait.until(EC.element_to_be_clickable(self.role_dropdown))
        dropdown.click()
        time.sleep(2)  # wait for dropdown options to appear

        # Select specific role from dropdown options
        option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='option']/span[text()='{role_text}']"))
        )
        option.click()

    def enter_employee_name(self, enter_employee_name):
        """
        Enters employee name in auto-suggestion field.
        """
        emp_field = self.wait.until(EC.presence_of_element_located(self.employee_name_field))
        emp_field.clear()
        emp_field.send_keys(enter_employee_name)
        time.sleep(2)  # wait for suggestions
        return emp_field.send_keys()

    def select_status(self, dropdown_value):
        """
        Selects user status from the Status dropdown.
        """
        select_option = self.wait.until(EC.element_to_be_clickable(self.select_element_status))
        select_option.click()
        time.sleep(2)

        enable_option = self.wait.until(EC.element_to_be_clickable(self.enable_select_element))
        enable_option.click()

    def drop_up_down_system_user(self):
        """
        Toggles the system user dropdown open and close.
        """
        dropdown = self.wait.until(EC.element_to_be_clickable(self.system_user_element))
        dropdown.click()
        time.sleep(2)
        dropdown.click()

    def click_on_search_button(self):
        """
        Clicks on the Search button to filter users.
        """
        self.wait.until(EC.element_to_be_clickable(self.search_button)).click()

    def click_reset_button(self):
        """
        Clicks on Reset button to clear all search filters.
        """
        self.wait.until(EC.element_to_be_clickable(self.reset_button)).click()

    def select_first_user_checkbox(self):
        """
        Selects the checkbox of the first user from the result table.
        """
        checkbox = self.wait.until(EC.element_to_be_clickable(self.user_checkbox))
        checkbox.click()

    def click_delete_button(self):
        """
        Clicks on the Delete button for the selected user.
        """
        delete_btn = self.wait.until(EC.element_to_be_clickable(self.delete_button))
        delete_btn.click()

    def click_confirm_deletion(self):
        """
        Confirms user deletion in the popup dialog.
        """
        confirm_btn = self.wait.until(EC.element_to_be_clickable(self.confirm_delete))
        confirm_btn.click()

    def get_search_result(self):
        """
        Returns the list of user rows displayed after search.
        """
        self.wait.until(EC.presence_of_element_located(self.result_rows))
        return self.driver.find_elements(*self.result_rows)
