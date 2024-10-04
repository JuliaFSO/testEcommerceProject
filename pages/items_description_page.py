from pages.base_page import BasePage
from pages.items_description_page_locators import ItemsDescriptionPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class ItemsDescriptionPage(BasePage):

    def change_hoodies_options(self):
        size = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                     ItemsDescriptionPageLocators.CHANGE_HOODIES_SIZE)
        color = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                      ItemsDescriptionPageLocators.CHANGE_HOODIES_COLOR)
        color.click()
        size.click()

    def change_pants_options(self):
        size = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                     ItemsDescriptionPageLocators.CHANGE_PANTS_SIZE)
        color = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                      ItemsDescriptionPageLocators.CHANGE_PANTS_COLOR)
        color.click()
        size.click()

    def change_shorts_options(self):
        size = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                     ItemsDescriptionPageLocators.CHANGE_SHORTS_SIZE)
        color = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                      ItemsDescriptionPageLocators.CHANGE_SHORTS_COLOR)
        color.click()
        size.click()

    def change_jackets_options(self):
        size = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                     ItemsDescriptionPageLocators.CHANGE_JACKETS_SIZE)
        color = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                      ItemsDescriptionPageLocators.CHANGE_JACKETS_COLOR)
        size.click()
        color.click()

    def wait_and_click_add_to_cart(self):
        add_cart_btn = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                             ItemsDescriptionPageLocators.ADD_CART_BTN)
        add_cart_btn.click()

    def get_added_to_cart_label(self):
        lbl_added_to_cart_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, ItemsDescriptionPageLocators.ADDED_TO_CART_MSG).text
        return lbl_added_to_cart_txt

    def navigate_previous_items(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, ItemsDescriptionPageLocators.BACK_ITEMS_LINK).click()
