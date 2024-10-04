from pages.base_page import BasePage
from pages.place_order_success_page_locators import PlaceOrderSuccessLocators
from resources.constants import MAX_WAIT_INTERVAL


class PlaceOrderSuccessPage(BasePage):

    def get_place_order_success_label(self):
        lbl_place_order_success_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, PlaceOrderSuccessLocators.PLACE_ORDER_SUCCESS_LBL).text
        print(lbl_place_order_success_txt)
        return lbl_place_order_success_txt
