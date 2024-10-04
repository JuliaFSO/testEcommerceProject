from pages.place_order_page import PlaceOrderPage
from pages.place_order_success_page import PlaceOrderSuccessPage
from resources.constants import PLACE_ORDER_SUCCESS_TEXT


class TestPlaceOrder:

    # Test Case 5 (Placing Order)
    def test_place_order(self, driver, shipping_address):
        place_order_page = PlaceOrderPage(driver)

        place_order_page.wait_and_click_next_btn()
        place_order_page.wait_and_click_place_order_btn()

        place_order_success_page = PlaceOrderSuccessPage(driver)

        lbl_place_order_success_txt = place_order_success_page.get_place_order_success_label()

        assert lbl_place_order_success_txt.__contains__(PLACE_ORDER_SUCCESS_TEXT), \
            "Place order failed!"
