import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from engines.drivers.selenium_driver import MySeleniumDriver


@pytest.fixture(scope="session")
def browser():
    # driver = MySeleniumDriver(webdriver.Chrome(executable_path=r'C:\Users\Irina\PycharmProjects\lib\chromedriver.exe'))
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    yield driver
    driver.quit()
