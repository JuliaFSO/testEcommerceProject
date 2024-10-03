from selenium.webdriver.common.by import By


class PlaceOrderPageLocators:

    FORM_PLACE_ORDER = (By.ID, "checkout-step-shipping")
    EMAIL_INPUT = (By.ID, "customer-email")
    PASSWORD_INPUT = (By.ID, "customer-password")
    SHIP_METHOD_RADIO = (By.CLASS_NAME, "col col-method")
    COUNTRY_SELECT = (By.NAME, "country_id")
    STATE_SELECT = (By.NAME, "region_id")
    NEXT_BTN = (By.ID, "shipping-method-buttons-container")
    PLACE_ORDER_BTN = (By.XPATH, "//*[@id='checkout-payment-method-load']/div/div/div[2]/div[2]/div[4]/div/button")
    PLACE_ORDER_SUCCESS_LBL = (By.XPATH, "//*[@id='maincontent']/div[1]/h1/span")
