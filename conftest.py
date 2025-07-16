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
    else:
        raise Exception("Only Chrome browser is supported for now.")

    driver.maximize_window()
    driver.get(url)
    time.sleep(4)
    request.cls.driver = driver
    yield
    driver.quit()

