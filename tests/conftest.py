import pytest
from selenium import webdriver
from engines.drivers.selenium_driver import SeleniumDriver


@pytest.fixture(scope="session")
def browser():
    driver = SeleniumDriver(webdriver.Chrome(executable_path=r'/Users/iryna.yeltsova/chromedriver'))
    driver.go_to_page()
    yield driver
    driver.quit()
