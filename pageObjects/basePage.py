from selenium import webdriver


class BasePage:
    """
    BasePage contains reusable common methods
    which can be inherited by all page classes.
    """

    driver = webdriver.Chrome

    def find(self, locator):
        # Find a web element using provided locator
        return self.driver.find_element(locator)

    def clear_element(self, locator):
        # Clear input field before entering new value
        self.driver.find_element(locator).clear()

    def send_values(self, locator, value):
        # Clear field and send input value
        self.clear_element(locator)
        self.driver.find_element(locator).send_keys(value)

    def click_on_element(self, locator):
        # Perform click action on element
        self.driver.find_element(locator).click()

    def get_text(self, locator):
        # Get visible text of an element
        return self.driver.find_element(locator).text
