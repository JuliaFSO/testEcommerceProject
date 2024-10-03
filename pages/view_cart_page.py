from pages.base_page import BasePage
from pages.view_cart_page_locators import ViewCartPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class ViewCartPage(BasePage):

    def wait_and_click_remove_item(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, ViewCartPageLocators.REMOVE_BTN).click()

    def wait_and_click_checkout_btn(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, ViewCartPageLocators.CHECKOUT_BTN).click()

    def wait_and_click_proceed_checkout_btn(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, ViewCartPageLocators.PROCEED_CHECKOUT_BTN).click()
