import os
import time
import pytest
from selenium import webdriver
import configparser

@pytest.fixture(scope="class")
def setup(request):
    config = configparser.ConfigParser()
    config.read("config/config.ini")

    url = config["DEFAULT"]["baseurl"]
    browser = config["DEFAULT"]["browser"]

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Only Chrome browser is supported for now.")

    driver.maximize_window()
    driver.get(url)
    time.sleep(4)
    request.cls.driver = driver
    yield driver
    driver.quit()



# screenshot
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.cls.driver
        screenShots_dir = "screenshots"
        os.makedirs(screenShots_dir,exist_ok=True)

        file_name = os.path.join(screenShots_dir,f"{item.name}.png")
        driver.save_screenshot(file_name)



