from pages.base_page import BasePage
from pages.women_pants_page_locators import WomenPantsPageLocators
from resources.constants import MAX_WAIT_INTERVAL
from actions.mouse_actions import MouseActions


class WomenPantsPage(BasePage):

    def wait_and_select_first_item(self):
        mouse_actions = MouseActions(self.driver)
        item = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, WomenPantsPageLocators.WOMEN_PANTS_ITEM1)
        mouse_actions.hover_over_element(item)
        item.click()

    def wait_and_select_second_item(self):
        mouse_actions = MouseActions(self.driver)
        item = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, WomenPantsPageLocators.WOMEN_PANTS_ITEM2)
        mouse_actions.hover_over_element(item)
        item.click()
