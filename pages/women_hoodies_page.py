from pages.base_page import BasePage
from pages.women_hoodies_page_locators import WomenHoodiesPageLocators
from resources.constants import MAX_WAIT_INTERVAL
from actions.mouse_actions import MouseActions


class WomenHoodiesPage(BasePage):

    def wait_and_select_hoodies_item(self):
        mouse_actions = MouseActions(self.driver)
        hoodies_item = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, WomenHoodiesPageLocators.
                                                             WOMEN_HOODIES_ITEM1)
        mouse_actions.hover_over_element(hoodies_item)
        hoodies_item.click()
