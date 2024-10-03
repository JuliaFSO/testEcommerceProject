from selenium.webdriver.common.action_chains import ActionChains


class MouseActions:

    def __init__(self, driver):
        self.action = ActionChains(driver)

    def hover_over_element(self, element):
        self.action.move_to_element(element).perform()
