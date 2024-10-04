import pytest as pytest
from selenium import webdriver
from tests.test_02_add_men_items import TestAddMenItems
from tests.test_01_add_women_items import TestAddWomenItems
from pages.view_cart_page import ViewCartPage
from pages.index_page import IndexPage


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def username_password():
    username = "john_doe@email.com"
    password = "JoHn123"
    return [username, password]


@pytest.fixture(scope="function")
def shipping_address():
    shipping_info = {
        "firstname": "John",
        "lastname": "Doe",
        "company": "XYZ",
        "street[0]": "12 Main St",
        "city": "Toronto",
        "region_id": "Ontario",
        "postcode": "A1B2C3",
        "country_id": "Canada",
        "telephone": "8885559636",
    }

    return shipping_info


@pytest.fixture(scope="function")
def setup_cart(driver):
    TestAddMenItems().test_adding_jackets_items(driver)
    index_page = IndexPage(driver)
    index_page.wait_and_click_view_cart_link()

    return driver


@pytest.fixture(scope="function")
def setup_place_order(driver):
    TestAddWomenItems().test_adding_hoodies_items(driver)

    index_page = IndexPage(driver)
    index_page.wait_and_click_view_cart_link()

    view_cart_page = ViewCartPage(driver)
    view_cart_page.wait_and_click_checkout_btn()
    view_cart_page.wait_and_click_proceed_checkout_btn()

    return driver
