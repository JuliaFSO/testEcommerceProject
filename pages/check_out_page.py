from pages.base_page import BasePage
from pages.check_out_page_locators import CheckOutPageLocators
from selenium.webdriver.common.by import By
from resources.constants import MAX_WAIT_INTERVAL


class CheckOutPage(BasePage):

    def fill_out_info(self, account_info):
        for info, value in account_info.items():
            input_locator = (By.NAME, info)
            self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, input_locator).send_keys(value)

    def click_place_order_btn(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CheckOutPageLocators.PLACE_ORDER_BTN).click()
