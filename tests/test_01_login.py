from pages.index_page import IndexPage
from pages.login_page import LoginPage
from resources.constants import TEST_SITE_URL


class TestLogin:

    # Test Case 1 ( Login )
    def test_login_user(self, driver, username_password):
        index_page1 = IndexPage(driver)
        index_page1.navigate_to(TEST_SITE_URL)

        # Navigate to Sign In Link
        index_page1.wait_and_click_sign_in_link()

        # Fill out form
        login_page = LoginPage(driver)
        login_page.wait_and_type_email(username_password)
        login_page.wait_and_type_password(username_password)

        # Click on submit button
        login_page.wait_and_click_sign_in_btn()

        # Login Success
        assert login_page.is_login_success(), "Login failed!"
