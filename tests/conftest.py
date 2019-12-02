import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from engines.drivers.selenium_driver import SeleniumDriver


@pytest.fixture(scope="session")
def browser():
    driver = SeleniumDriver(webdriver.Chrome(executable_path=ChromeDriverManager().install()))
    driver.go_to_page()

    yield driver
    driver.quit()
