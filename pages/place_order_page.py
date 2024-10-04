from pages.base_page import BasePage
from pages.place_order_page_locators import PlaceOrderPageLocators
from resources.constants import MAX_WAIT_INTERVAL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class PlaceOrderPage(BasePage):

    def wait_and_click_place_order_btn(self):
        place_order_btn = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                PlaceOrderPageLocators.PLACE_ORDER_BTN)
        place_order_btn.click()

    def wait_and_click_next_btn(self):
        next_btn = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, PlaceOrderPageLocators.NEXT_BTN)
        next_btn.click()

    def fill_out_user_info(self, usr_and_pw):
        email_field = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, PlaceOrderPageLocators.EMAIL_INPUT)
        time.sleep(2)
        email_field.send_keys(usr_and_pw[0])
        time.sleep(2)
        password_field = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, PlaceOrderPageLocators.PASSWORD_INPUT)
        time.sleep(1)
        password_field.send_keys(usr_and_pw[1])

    def fill_out_shipping_info(self, ship_info):
        form = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, PlaceOrderPageLocators.FORM_PLACE_ORDER)

        for info, value in ship_info.items():
            form.find_element(By.NAME, info).send_keys(value)

        country_dropdown = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                 PlaceOrderPageLocators.COUNTRY_SELECT)

        dropdownSelect = Select(country_dropdown)
        dropdownSelect.select_by_value("CA")

        state_dropdown = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                               PlaceOrderPageLocators.STATE_SELECT)

        dropdownSelect = Select(state_dropdown)
        dropdownSelect.select_by_value("74")

        ship_method_radio = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, PlaceOrderPageLocators.
                                                                  SHIP_METHOD_RADIO)
        ship_method_radio.click()

        submit_btn = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, PlaceOrderPageLocators.SUBMIT_BTN)
        submit_btn.click()

    def get_place_order_success_label(self):
        lbl_place_order_success_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, PlaceOrderPageLocators.PLACE_ORDER_SUCCESS_LBL).text
        return lbl_place_order_success_txt
