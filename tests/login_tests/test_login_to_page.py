from page_objects.constants import EXPECTED_ALERT_MESSAGE
from page_objects.pages.login_page import LoginPage, alert_message

#
# def test_login_to_the_ukr_net_page_with_wrong_credentials(browser):
#     """ The test check that the warning message appears with not valid filled credentials """
#     login_page = LoginPage(browser)
#     login_page.fill_login(user_name="user")
#     login_page.fill_password(password="password")
#     login_page.submit_button()
#     assert alert_message == EXPECTED_ALERT_MESSAGE
