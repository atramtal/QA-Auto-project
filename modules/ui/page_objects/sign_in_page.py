from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = "https://github.com/login"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # find field where to input wrong password
        login_elem = self.driver.find_element(By.ID, "login_field")

        # enter wrong user name
        login_elem.send_keys(username)

        # find password field
        pass_elem = self.driver.find_element(By.ID, "password")

        # enter wrong password
        pass_elem.send_keys(password)

        # find sign in button
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # mouse click
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
        