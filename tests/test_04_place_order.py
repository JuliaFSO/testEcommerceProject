from pages.place_order_page import PlaceOrderPage
from resources.constants import PLACE_ORDER_SUCCESS_TEXT
from tests.test_utils import *


class TestPlaceOrder:

    # Test Case 4 (Placing Order)
    def test_place_order(self, driver, username_password, shipping_address):
        place_order_page = PlaceOrderPage(driver)

        place_order_page.fill_out_username_password(username_password)
        place_order_page.fill_out_info(shipping_address)

        place_order_page.wait_and_click_next_btn()
        place_order_page.wait_and_click_place_order_btn()

        lbl_place_order_success_txt = place_order_page.get_place_order_success_label()
        assert lbl_place_order_success_txt.__contains__(PLACE_ORDER_SUCCESS_TEXT), \
            "Adding first hoodie item to cart failed!"
