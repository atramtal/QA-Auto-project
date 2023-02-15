from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # create page object
    sign_in_page = SignInPage()

    # open page
    sign_in_page.go_to()

    # try to enter in to the system
    sign_in_page.try_login("page_object@gmail.com", "123456wrong password")

    # check user name page title is the same as expected
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # close browser
    sign_in_page.close()
