from pages.index_page import IndexPage
from tests.test_utils import *
from pages.men_shorts_page import MenShortsPage
from pages.men_jackets_page import MenJacketsPage
from pages.items_description_page import ItemsDescriptionPage
from resources.constants import ADDED_TO_CART_TEXT
from resources.constants import TEST_SITE_URL


class TestAddMenItems:

    # Test Case 1 (Adding men items to the Cart)
    def test_adding_jackets_items(self, driver):
        index_page1 = IndexPage(driver)

        index_page1.navigate_to(TEST_SITE_URL)
        index_page1.wait_and_click_men_jackets_link()

        # Select and add the first item to the cart
        men_jackets_page1 = MenJacketsPage(driver)
        men_jackets_page1.wait_and_select_first_item()

        men_jackets_item_page1 = ItemsDescriptionPage(driver)
        men_jackets_item_page1.change_jackets_options()
        men_jackets_item_page1.wait_and_click_add_to_cart()

        lbl_added_to_cart_txt1 = men_jackets_item_page1.get_added_to_cart_label()
        assert lbl_added_to_cart_txt1.__contains__(ADDED_TO_CART_TEXT), "Adding first jacket item to cart failed!"

        # Navigate home
        index_page1.navigate_home()

    def test_adding_shorts_items(self, driver):
        index_page2 = IndexPage(driver)
        index_page2.wait_and_click_men_shorts_link()

        # Select and add the second item to the cart
        men_shorts_page1 = MenShortsPage(driver)
        men_shorts_page1.wait_and_select_first_item()

        men_shorts_item_page1 = ItemsDescriptionPage(driver)
        men_shorts_item_page1.change_shorts_options()
        men_shorts_item_page1.wait_and_click_add_to_cart()

        lbl_added_to_cart_txt1 = men_shorts_item_page1.get_added_to_cart_label()
        assert lbl_added_to_cart_txt1.__contains__(ADDED_TO_CART_TEXT), "Adding first shorts item to cart failed!"

        # Navigate home
        index_page2.navigate_home()
