from pages.base_page import BasePage
from pages.place_order_page_locators import PlaceOrderPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class PlaceOrderPage(BasePage):

    def wait_and_click_place_order_btn(self):
        place_order_btn = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                PlaceOrderPageLocators.PLACE_ORDER_BTN)
        place_order_btn.click()

    def wait_and_click_next_btn(self):
        next_btn = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, PlaceOrderPageLocators.NEXT_BTN)
        next_btn.click()
