from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SeleniumDriver(object):

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://ukr.net"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_page(self):
        return self.driver.get(self.base_url)

    def get_page_title(self):
        """Return a title of the current page """
        return self.driver.title

    def close(self):
        """ Close the browser """
        return self.driver.close()

    def maximize_window(self):
        """ Maximize the browser window """
        self.driver.maximize_window()
