from pages.base_page import BasePage
from pages.women_hoodies_page_locators import WomenHoodiesPageLocators
from resources.constants import MAX_WAIT_INTERVAL
from actions.mouse_actions import MouseActions


class WomenHoodiesPage(BasePage):

    def wait_and_select_first_item(self):
        mouse_actions = MouseActions(self.driver)
        item = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, WomenHoodiesPageLocators.WOMEN_HOODIES_ITEM1)
        mouse_actions.hover_over_element(item)
        item.click()

    def wait_and_select_second_item(self):
        mouse_actions = MouseActions(self.driver)
        item = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, WomenHoodiesPageLocators.WOMEN_HOODIES_ITEM2)

        mouse_actions.hover_over_element(item)
        item.click()
