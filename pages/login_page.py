from pages.base_page import BasePage
from pages.login_page_locators import LoginPageLocators
from resources.constants import MAX_WAIT_INTERVAL
import time


class LoginPage(BasePage):

    def wait_and_type_first_name(self, user_info):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginPageLocators.FIRST_NAME_INPUT).send_keys(
            user_info["firstname"])

    def wait_and_type_last_name(self, user_info):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginPageLocators.LAST_NAME_INPUT).send_keys(
            user_info["lastname"])

    def wait_and_type_email(self, username_password):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginPageLocators.EMAIL_INPUT).send_keys(
            username_password[0])

    def wait_and_type_password(self, username_password):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginPageLocators.PASSWORD_INPUT).send_keys(
            username_password[1])

    def wait_and_type_password_confirm(self, user_info):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(
            user_info["password_confirmation"])

    def wait_and_click_sign_in_btn(self):
        self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, LoginPageLocators.SIGN_IN_BTN).click()
        time.sleep(3)

    def wait_and_click_create_account_btn(self):
        self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, LoginPageLocators.CREATE_ACCOUNT_BTN).click()

    def is_login_success(self):
        success_element = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, LoginPageLocators.LOGIN_ELEM
        )
        return True if success_element else False
