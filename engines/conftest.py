import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def app():
    driver = webdriver.Chrome(executable_path=r'/Users/iryna.yeltsova/Downloads/chromedriver')
    yield driver
    driver.quit()
