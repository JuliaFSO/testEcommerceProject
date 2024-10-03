from pages.base_page import BasePage
from pages.check_out_page_locators import CheckOutPageLocators
from selenium.webdriver.common.by import By


class CheckOutPage(BasePage):

    def fill_out_info(self, account_info):
        for info, value in account_info.items():
            input_locator = (By.NAME, info)
            self.find_element(input_locator).send_keys(value)

    def click_place_order_btn(self):
        self.find_element(CheckOutPageLocators.PLACE_ORDER_BTN).click()
