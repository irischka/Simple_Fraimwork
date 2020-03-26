from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from engines.elements.web_element import WebElement
from page_objects.locators.login_locators import *


class SeleniumDriver:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://ukr.net"

    def find_element(self, locator, time=10):
        return WebElement(WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator)))

    def find_elements(self, locator, time=10):
        return WebElement(WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator)))

    def go_to_page(self):
        return self.driver.get(self.base_url)

    def get_page_title(self):
        """Return a title of the current page """
        return self.driver.title

    def close(self):
        """ Close the browser """
        return self.driver.close()

    def quit(self):
        """ Close the browser """
        return self.driver.quit()

    def maximize_window(self):
        """ Maximize the browser window """
        self.driver.maximize_window()

    def frame_switch(self, parameter):
        # return self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR,'#'+frame_login[1]))
        # return self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, "#login-frame-wraper > iframe"))
        return self.driver.switch_to.frame(parameter)
