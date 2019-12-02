from page_objects.locators.login_locators import *


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_login(self, user_name):
        self.driver.switch_to()
        input_field = self.driver.find_element(email_field)
        input_field.clear()
        input_field.input(user_name)

    def fill_password(self, password):
        input_field = self.driver.find_element(password_field)
        input_field.clear()
        input_field.input(password)

    def submit_button(self):
        button = self.driver.find_element(login_button)
        button.click()

    def get_text_submit_button(self):
        input_field = self.driver.find_element(login_button)
        return input_field.value()

