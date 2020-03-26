from page_objects.locators.search_locators import *


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_query(self, world):
        input_field = self.driver.find_element(SEARCH_INPUT)
        input_field.clear()
        input_field.input(world)

    def submit_query(self):
        button = self.driver.find_element(SEARCH_BUTTON)
        button.click()

    def get_text_query(self):
        input_field = self.driver.find_element(SEARCH_INPUT)
        return input_field.value()

    def get_page_title(self):
        return self.get_page_title()

    def get_text_search_button(self):
        input_field = self.driver.find_element(SEARCH_BUTTON)
        return input_field.value()


