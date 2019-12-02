from selenium.webdriver.common.keys import Keys


class WebElement:

    def __init__(self, element):
        self.element = element

    def click(self):
        """ Click the element """
        self.element.click()

    def clear(self):
        """ Clear the text if it is a text entry element """
        self.element.clear()

    def input(self, text):
        """ Set value for given string """
        self.element.send_keys(text)

    def value(self) -> str:
        """ Get attribute value """
        return self.element.get_attribute("value")

    def get_attribute_text(self) -> str:
        """ Get attribute text """
        return self.element.get_attribute("text")

    def get_element_text(self) -> str:
        """ Get element text from label """
        return self.element.text

    def submit_request(self):
        """ Click enter """
        self.element.send_keys(Keys.ENTER)
