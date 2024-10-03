from pages.view_cart_page import ViewCartPage
from tests.test_utils import *


class TestEditCart:

    # Test Case 3 (Editing Cart)
    def test_edit_cart(self, driver):
        view_cart_page = ViewCartPage(driver)
        view_cart_page.wait_and_click_checkout_btn()
        view_cart_page.wait_and_click_remove_item()
        view_cart_page.wait_and_click_proceed_checkout_btn()
