from selenium.webdriver.common.by import By

email_field = (By.ID, "id-input-login")
password_field = (By.ID, "id-input-password")
login_button = (By.CSS_SELECTOR, "button.form__submit")
alert_message = (By.CSS_SELECTOR, ".alert.alert-danger")
iframe = (By.CSS_SELECTOR, "login-frame-wraper > iframe")
