from page_objects.constants import EXPECTED_ALERT_MESSAGE
from page_objects.pages.login_page import LoginPage


def test_login_to_the_ukr_net_page_with_wrong_credentials(browser):
    """ The test check that the warning message appears with not valid filled credentials """

    "Step: Navigate to the Login Page"
    login_page = LoginPage(browser)

    "Step:Enter 'valid_email' in the Email Address field"
    login_page.fill_login(user_name="user")

    "Click the Submit button"
    login_page.submit_button()

    "Enter 'valid_password' in the Password field"
    login_page.fill_password(password="password")

    "Click the Submit button"
    login_page.submit_button()

    "Verify that the message 'Неправильні дані' is displayed"
    text = login_page.get_text_alert_message()
    assert text == EXPECTED_ALERT_MESSAGE
