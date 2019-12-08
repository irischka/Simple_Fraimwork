from selenium.webdriver.common.by import By

email_field = (By.CSS_SELECTOR, "input#id-input-login")
password_field = (By.ID, "id-input-password")
login_button = (By.CSS_SELECTOR, "button.form__submit")
alert_message = (By.CSS_SELECTOR, ".form__error.form__error_wrong.form__error_visible")
frame_login = (By.CSS_SELECTOR, "#login-frame-wraper > iframe")
