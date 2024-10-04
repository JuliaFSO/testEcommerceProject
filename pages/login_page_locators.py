from selenium.webdriver.common.by import By


class LoginPageLocators:

    FORM_REGISTER = (By.XPATH, "//*[@id='form-validate']")
    FIRST_NAME_INPUT = (By.NAME, "firstname")
    LAST_NAME_INPUT = (By.NAME, "lastname")
    EMAIL_INPUT = (By.NAME, "login[username]")
    PASSWORD_INPUT = (By.NAME, "login[password]")
    CONFIRM_PASSWORD_INPUT = (By.NAME, "password_confirmation")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//*[@id='form-validate']/div/div[1]/button")
    SIGN_IN_BTN = (By.ID, "send2")
    LOGIN_ELEM = (By.CLASS_NAME, "logged-in")
