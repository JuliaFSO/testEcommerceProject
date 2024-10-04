from pages.base_page import BasePage
from pages.index_page_locators import IndexPageLocators
from resources.constants import MAX_WAIT_INTERVAL
from actions.mouse_actions import MouseActions


# index page
class IndexPage(BasePage):

    def wait_and_click_create_account_link(self):
        create_account_btn = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                   IndexPageLocators.CREATE_ACCOUNT_LINK)
        create_account_btn.click()

    def wait_and_click_sign_in_link(self):
        create_account_btn = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                   IndexPageLocators.SIGN_IN_LINK)
        create_account_btn.click()

    def wait_and_click_women_hoodies_link(self):
        mouse_actions = MouseActions(self.driver)

        women_dropdown = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.WOMEN_DROPDOWN)
        women_tops_link = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.WOMEN_TOPS_LINK)
        women_hoodies_link = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                   IndexPageLocators.WOMEN_HOODIES_LINK)

        mouse_actions.hover_over_element(women_dropdown)
        mouse_actions.hover_over_element(women_tops_link)
        mouse_actions.hover_over_element(women_hoodies_link)

        women_hoodies_link.click()

    def wait_and_click_women_pants_link(self):
        mouse_actions = MouseActions(self.driver)

        women_dropdown = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.WOMEN_DROPDOWN)
        women_bottoms_link = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                   IndexPageLocators.WOMEN_BOTTOMS_LINK)
        women_pants_link = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                 IndexPageLocators.WOMEN_PANTS_LINK)

        mouse_actions.hover_over_element(women_dropdown)
        mouse_actions.hover_over_element(women_bottoms_link)
        mouse_actions.hover_over_element(women_pants_link)

        women_pants_link.click()

    def wait_and_click_men_shorts_link(self):
        mouse_actions3 = MouseActions(self.driver)

        men_dropdown = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.MEN_DROPDOWN)
        men_bottoms_link = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.MEN_BOTTOMS_LINK)
        men_shorts_link = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.MEN_SHORTS_LINK)

        mouse_actions3.hover_over_element(men_dropdown)
        mouse_actions3.hover_over_element(men_bottoms_link)
        mouse_actions3.hover_over_element(men_shorts_link)

        men_shorts_link.click()

    def wait_and_click_men_jackets_link(self):
        mouse_actions4 = MouseActions(self.driver)

        men_dropdown = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.MEN_DROPDOWN)
        men_tops_link = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.MEN_TOPS_LINK)
        men_jackets_link = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.MEN_JACKETS_LINK)

        mouse_actions4.hover_over_element(men_dropdown)
        mouse_actions4.hover_over_element(men_tops_link)
        mouse_actions4.hover_over_element(men_jackets_link)

        men_jackets_link.click()

    def navigate_home(self):
        self.find_element(IndexPageLocators.HOME).click()

    def wait_and_click_view_cart_link(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.VIEW_CART_BTN).click()
