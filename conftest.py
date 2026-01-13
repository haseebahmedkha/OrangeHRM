# Import necessary modules
import os  # For creating directories and handling file paths
import time  # For adding sleep/wait
import pytest  # PyTest framework
from selenium import webdriver  # Selenium WebDriver
import configparser  # To read configuration from .ini files



# ================================
# PyTest fixture to setup Selenium WebDriver
# ================================
# Scope is "function", meaning the browser will open before each test function and close after it
@pytest.fixture(scope="function")
def setup(request):
    """
    Initializes the browser before each test and quits after test completion.

    :param request: PyTest built-in fixture used to access the test class
    """

    # Load configuration from config.ini
    config = configparser.ConfigParser()
    config.read("config/config.ini")

    # Read URL and browser type from the config file
    url = config["DEFAULT"]["baseurl"]
    browser = config["DEFAULT"]["browser"]

    # Initialize the browser based on config
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        # Raise exception if an unsupported browser is specified
        raise Exception("Only Chrome and Firefox browsers are supported for now.")

    # Maximize the browser window
    driver.maximize_window()

    # Open the target URL
    driver.get(url)

    # Optional sleep to wait for page load (can be replaced with explicit waits for better practice)
    time.sleep(4)

    # Assign the driver to the test class (if using class-based tests)
    request.cls.driver = driver

    # Yield the driver to the test function
    yield driver

    # Teardown: quit the browser after the test is finished
    driver.quit()
    # driver.close()  # Alternative to quit if you only want to close current window


# ================================
# PyTest hook to take screenshot on test failure
# ================================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to execute after each test and capture screenshot if test fails.

    :param item: Test item (function/class)
    :param call: Test execution information
    """

    # Yield to get the test report
    outcome = yield
    report = outcome.get_result()

    # Check if the test call has failed
    if report.when == "call" and report.failed:
        # Access the WebDriver instance from the test class
        driver = item.cls.driver

        # Create screenshots directory if it doesn't exist
        screenShots_dir = "screenshots"
        os.makedirs(screenShots_dir, exist_ok=True)

        # Define screenshot file name using test function name
        file_name = os.path.join(screenShots_dir, f"{item.name}.png")

        # Save screenshot of the current browser window
        driver.save_screenshot(file_name)
