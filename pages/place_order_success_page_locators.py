from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PlaceOrderSuccessLocators(BasePage):

    PLACE_ORDER_SUCCESS_LBL = (By.XPATH, "//*[@id='maincontent']/div[3]/div/div[2]/p[1]")
