from selenium.webdriver.common.by import By

EMAIL_FIELD = (By.CSS_SELECTOR, "input#id-input-login")
PASSWORD_FIELD = (By.ID, "id-input-password")
LOGIN_BUTTON = (By.CSS_SELECTOR, "button.form__submit")
ALERT_MESSAGE = (By.CSS_SELECTOR, ".form__error.form__error_wrong.form__error_visible")
FRAME_LOGIN = (By.CSS_SELECTOR, "#login-frame-wraper > iframe")
