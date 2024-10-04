from selenium.webdriver.common.by import By


# index locators
class IndexPageLocators:

    HOME = (By.XPATH, "/html/body/div[2]/header/div[2]/a")
    SIGN_IN_LINK = (By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[2]/a")
    CREATE_ACCOUNT_LINK = (By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[3]/a")
    VIEW_CART_BTN = (By.XPATH, "/html/body/div[2]/header/div[2]/div[1]/a")
    LOGIN_SUCCESS_TEXT = (By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[1]/span")

    WOMEN_DROPDOWN = (By.ID, "ui-id-4")
    WOMEN_TOPS_LINK = (By.ID, "ui-id-9")
    WOMEN_HOODIES_LINK = (By.ID, "ui-id-12")
    WOMEN_BOTTOMS_LINK = (By.ID, "ui-id-10")
    WOMEN_PANTS_LINK = (By.ID, "ui-id-15")

    MEN_DROPDOWN = (By.ID, "ui-id-5")
    MEN_TOPS_LINK = (By.ID, "ui-id-17")
    MEN_JACKETS_LINK = (By.ID, "ui-id-19")
    MEN_BOTTOMS_LINK = (By.ID, "ui-id-18")
    MEN_SHORTS_LINK = (By.ID, "ui-id-24")
