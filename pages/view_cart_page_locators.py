from selenium.webdriver.common.by import By


# View Cart page locators
class ViewCartPageLocators:

    CHECKOUT_BTN = (By.XPATH, "/html/body/div[2]/header/div[2]/div[1]/a")
    VIEW_CART_BTN = (By.XPATH, "//*[@id='minicart-content-wrapper']/div[2]/div[5]/div/a")
    REMOVE_BTN = (By.XPATH, "//*[@id='shopping-cart-table']/tbody[1]/tr[2]/td/div/a[2]")
    CART_BTN = (By.XPATH, "/html/body/div[2]/header/div[2]/div[1]/a")
    PROCEED_CHECKOUT_BTN = (By.XPATH, "//*[@id='maincontent']/div[3]/div/div[2]/div[1]/ul/li[1]/button")
    CART_ITEMS_COUNT = (By.CLASS_NAME, "count")

