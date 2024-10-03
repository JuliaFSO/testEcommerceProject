from selenium.common import NoSuchElementException

from pages.base_page import BasePage
from pages.items_description_page_locators import ItemsDescriptionPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class ItemsDescriptionPage(BasePage):

    def colors_options(self, color1_locator, color2_locator):
        try:
            color1 = self.find_element(color1_locator)
            color1.click()
        except NoSuchElementException:
            print('Error: Color 1 not available.')

        try:
            color2 = self.find_element(color2_locator)
            color2.click()
        except NoSuchElementException:
            print('Color 2 not available; only Color 1 selected.')

    def change_hoodies_options(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                              ItemsDescriptionPageLocators.CHANGE_HOODIES_SIZE).click()
        self.colors_options(ItemsDescriptionPageLocators.CHANGE_HOODIES_COLOR1,
                            ItemsDescriptionPageLocators.CHANGE_HOODIES_COLOR2)

    def change_pants_options(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                              ItemsDescriptionPageLocators.CHANGE_PANTS_SIZE).click()
        self.colors_options(ItemsDescriptionPageLocators.CHANGE_PANTS_COLOR1,
                            ItemsDescriptionPageLocators.CHANGE_PANTS_COLOR2)

    def change_shorts_options(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                              ItemsDescriptionPageLocators.CHANGE_SHORTS_SIZE).click()
        self.colors_options(ItemsDescriptionPageLocators.CHANGE_SHORTS_COLOR1,
                            ItemsDescriptionPageLocators.CHANGE_SHORTS_COLOR2)

    def change_jackets_options(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                              ItemsDescriptionPageLocators.CHANGE_JACKETS_SIZE).click()
        self.colors_options(ItemsDescriptionPageLocators.CHANGE_JACKETS_COLOR1,
                            ItemsDescriptionPageLocators.CHANGE_JACKETS_COLOR2)

    def wait_and_click_add_to_cart(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, ItemsDescriptionPageLocators.ADD_CART_BTN).click()

    def get_added_to_cart_label(self):
        lbl_added_to_cart_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, ItemsDescriptionPageLocators.ADDED_TO_CART_MSG).text
        return lbl_added_to_cart_txt

    def navigate_previous_items(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, ItemsDescriptionPageLocators.BACK_ITEMS_LINK).click()
