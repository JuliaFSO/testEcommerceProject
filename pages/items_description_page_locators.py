from selenium.webdriver.common.by import By


# items description locators
class ItemsDescriptionPageLocators:

    ADD_CART_BTN = (By.ID, "product-addtocart-button")
    ADDED_TO_CART_MSG = (By.XPATH, "//*[@id='maincontent']/div[1]/div[2]/div/div/div")

    # WOMEN HOODIES OPTIONS
    CHANGE_HOODIES_SIZE = (By.ID, "option-label-size-143-item-168")
    CHANGE_HOODIES_COLOR1 = (By.ID, "option-label-color-93-item-53")
    CHANGE_HOODIES_COLOR2 = (By.ID, "option-label-color-93-item-50")

    # WOMEN PANTS OPTIONS
    CHANGE_PANTS_SIZE = (By.ID, "option-label-size-143-item-172")
    CHANGE_PANTS_COLOR1 = (By.ID, "option-label-color-93-item-49")
    CHANGE_PANTS_COLOR2 = (By.ID, "option-label-color-93-item-50")

    # MEN SHORTS OPTIONS
    CHANGE_SHORTS_SIZE = (By.ID, "option-label-size-143-item-178")
    CHANGE_SHORTS_COLOR1 = (By.ID, "option-label-color-93-item-52")
    CHANGE_SHORTS_COLOR2 = (By.ID, "option-label-color-93-item-49")

    # MEN JACKETS OPTIONS
    CHANGE_JACKETS_SIZE = (By.ID, "option-label-size-143-item-169")
    CHANGE_JACKETS_COLOR1 = (By.ID, "option-label-color-93-item-57")
    CHANGE_JACKETS_COLOR2 = (By.ID, "option-label-color-93-item-58")

    # NAVIGATE TO PREVIOUS ITEMS LINK
    BACK_ITEMS_LINK = (By.XPATH, "/html/body/div[2]/div[2]/ul/li[4]/a")
