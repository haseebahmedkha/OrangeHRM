from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:
    """
    Page Object Model (POM) class for Admin module in OrangeHRM.
    This class contains locators and actions related to Admin → User Management.
    """

    # -------------------- Locators Section --------------------
    # These are XPath locators for elements used on the Admin page

    admin_menu = "//span[text()='Admin']"                      # Admin menu in left sidebar
    add_button = "//button[normalize-space()='Add']"           # Add button to create new user
    role_dropdown = "//label[text()='User Role']/following::div[1]//select"
    emp_name_input = "//input[@placeholder='Type for hints...']"
    user_input = "//label[text()='Username']/following::input[1]"
    status_dropdown = "//label[text()='Status']/following::div[1]//select"
    pass_input = "//label[text()='Password']/following::input[1]"
    confirm_password_input = "//label[text()='Confirm Password']/following::input[1]"
    save_button = "//button[normalize-space()='Save']"
    success_message = "//div[contains(@class,'oxd-toast') and contains(text(),'Success')]"


    def __init__(self, driver):
        """
        Constructor for AdminPage.
        Initializes WebDriver instance and explicit wait.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)


    def go_to_admin(self):
        """
        Navigates to the Admin section by clicking the Admin menu.
        Uses explicit wait to ensure element is clickable before interaction.
        """
        admin_element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.admin_menu))
        )
        admin_element.click()


    def click_on_add_button(self):
        """
        Clicks on the 'Add' button to open the user creation form.
        """
        admin_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.add_button))
        )
        admin_button.click()


    def select_role(self, role):
        """
        Selects user role from custom dropdown.
        Since OrangeHRM uses a custom UI dropdown,
        Select class cannot be used — we click manually.
        """

        # Open User Role dropdown
        dropdown = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[text()='User Role']/following::div[@class='oxd-select-wrapper'][1]")
            )
        )
        dropdown.click()

        # Select role based on visible text (e.g., Admin / ESS)
        option = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[@role='option']/span[text()='{role}']")
            )
        )
        option.click()


    def enter_emp_name(self, emp_name):
        """
        Enters employee name and selects it from auto-suggestion list.
        OrangeHRM shows suggestions dynamically, so explicit wait is required.
        """

        field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.emp_name_input))
        )
        field.clear()
        field.send_keys(emp_name)

        # Select employee from suggestion dropdown
        suggestion = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[@role='listbox']//span[contains(text(),'{emp_name.split()[0]}')]")
            )
        )
        suggestion.click()


    def enter_user_name(self, user_name):
        """
        Enters the username for the new user account.
        """
        field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.user_input))
        )
        field.clear()
        field.send_keys(user_name)


    def select_status(self, status):
        """
        Selects account status (Enabled / Disabled) from custom dropdown.
        """

        # Open Status dropdown
        dropdown = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[text()='Status']/following::div[@class='oxd-select-wrapper'][1]")
            )
        )
        dropdown.click()

        # Select desired status
        option = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[@role='option']/span[text()='{status}']")
            )
        )
        option.click()


    def enter_password(self, password):
        """
        Enters password for the new user.
        """
        field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.pass_input))
        )
        field.clear()
        field.send_keys(password)


    def confirm_password(self, confirm_password):
        """
        Enters confirmation password.
        """
        field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.confirm_password_input))
        )
        field.clear()
        field.send_keys(confirm_password)


    def click_on_save_button(self):
        """
        Clicks the Save button to submit user creation form.
        """
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.save_button))
        ).click()


    def is_success_message_displayed(self):
        """
        Validates whether success toast message appears after saving.
        Returns True if message is visible, otherwise False.
        """
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.success_message))
            )
            return True
        except:
            return False
