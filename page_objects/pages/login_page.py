from page_objects.locators.login_locators import *


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_login(self, user_name):
        self.driver.frame_switch_login_page()
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

    # def frame_switch_to_login(self):
    #     return self.driver.frame_switch(self.driver.find_element(frame_login))
    def frame_switch_login_page(self):
        return self.driver.frame_switch(self.driver.find_element(By.CSS_SELECTOR,'#'+frame_login[1]))
        # return self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, "#login-frame-wraper > iframe"))

    def get_text_alert_message(self):
        text_alert_message = self.driver.find_element(alert_message)
        return text_alert_message.get_element_text()

#
# class PageObgect:
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.login_input = None
#         self.button_login = None
#
#     def get_login_button(self):
#         self.driver.find_element(email_field)
#         return self.login_input

