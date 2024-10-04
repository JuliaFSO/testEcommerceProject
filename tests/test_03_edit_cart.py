from pages.view_cart_page import ViewCartPage
from tests.test_utils import *


class TestEditCart:

    # Test Case 3 (Editing Cart)
    def test_edit_cart(self, driver):
        view_cart_page = ViewCartPage(driver)
        view_cart_page.wait_and_click_checkout_btn()
        cart_items_count = view_cart_page.get_cart_items_count()
        view_cart_page.wait_and_click_view_cart_btn()
        view_cart_page.wait_and_click_remove_item()
        view_cart_page.wait_and_click_proceed_checkout_btn()

        assert cart_items_count != (cart_items_count - 1), "Editing cart failed!"
