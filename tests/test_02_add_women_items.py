from pages.index_page import IndexPage
from pages.women_pants_page import WomenPantsPage
from pages.women_hoodies_page import WomenHoodiesPage
from pages.items_description_page import ItemsDescriptionPage
from resources.constants import ADDED_TO_CART_TEXT


class TestAddWomenItems:
    # Test Case 2 (Adding women items to the Cart)
    def test_adding_hoodies_items(self, driver):
        index_page1 = IndexPage(driver)

        # Navigate to hoodies list
        index_page1.wait_and_click_women_hoodies_link()

        # Select the first item to the cart
        women_hoodies_page1 = WomenHoodiesPage(driver)
        women_hoodies_page1.wait_and_select_hoodies_item()

        # Select size and color of item
        women_hoodies_item_page1 = ItemsDescriptionPage(driver)
        women_hoodies_item_page1.change_hoodies_options()

        # Add item to the cart
        women_hoodies_item_page1.wait_and_click_add_to_cart()
        lbl_added_to_cart_txt1 = women_hoodies_item_page1.get_added_to_cart_label()

        assert lbl_added_to_cart_txt1.__contains__(ADDED_TO_CART_TEXT), "Adding hoodie item to cart failed!"

        # Navigate home
        index_page1.navigate_home()

    def test_adding_pants_items(self, driver):
        index_page2 = IndexPage(driver)

        # Navigate to pants list
        index_page2.wait_and_click_women_pants_link()

        # Select the second item to the cart
        women_pants_page1 = WomenPantsPage(driver)
        women_pants_page1.wait_and_select_pants_item()

        # Select size and color of item
        women_pants_item_page1 = ItemsDescriptionPage(driver)
        women_pants_item_page1.change_pants_options()

        # Add item to the cart
        women_pants_item_page1.wait_and_click_add_to_cart()
        lbl_added_to_cart_txt1 = women_pants_item_page1.get_added_to_cart_label()

        # Navigate home
        index_page2.navigate_home()

        assert lbl_added_to_cart_txt1.__contains__(ADDED_TO_CART_TEXT), "Adding pants item to cart failed!"
