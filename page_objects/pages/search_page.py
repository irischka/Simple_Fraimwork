from engines.drivers.selenium_driver import SeleniumDriver
from page_objects.locators.search_locators import *


class SearchPage(SeleniumDriver):

    def enter_query(self, world):
        input_field = self.find_element(search_input)
        input_field.clear()
        input_field.input(world)

    def submit_query(self):
        button = self.find_element(submit_button)
        button.click()

    def get_text(self):
        input_field = self.find_element(search_input)
        return input_field.value()

    def get_page_title(self):
        return self.get_page_title()
