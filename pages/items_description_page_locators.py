from selenium.webdriver.common.by import By


# items description locators
class ItemsDescriptionPageLocators:

    ADD_CART_BTN = (By.XPATH, "//*[@id='product-addtocart-button']")
    ADDED_TO_CART_MSG = (By.XPATH, "//*[@id='maincontent']/div[1]/div[2]/div/div/div")

    # WOMEN HOODIES OPTIONS
    CHANGE_HOODIES_SIZE = (By.ID, "option-label-size-143-item-168")
    CHANGE_HOODIES_COLOR = (By.ID, "option-label-color-93-item-53")

    # WOMEN PANTS OPTIONS
    CHANGE_PANTS_SIZE = (By.ID, "option-label-size-143-item-172")
    CHANGE_PANTS_COLOR = (By.ID, "option-label-color-93-item-49")

    # MEN SHORTS OPTIONS
    CHANGE_SHORTS_SIZE = (By.ID, "option-label-size-143-item-178")
    CHANGE_SHORTS_COLOR = (By.ID, "option-label-color-93-item-52")

    # MEN JACKETS OPTIONS
    CHANGE_JACKETS_SIZE = (By.ID, "option-label-size-143-item-169")
    CHANGE_JACKETS_COLOR = (By.ID, "option-label-color-93-item-52")

    # NAVIGATE TO PREVIOUS ITEMS LINK
    BACK_ITEMS_LINK = (By.XPATH, "/html/body/div[2]/div[2]/ul/li[4]/a")
