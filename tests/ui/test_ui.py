import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


@pytest.mark.ui
def test_check_incorrect_username():
    # create an object to controll a browser
    driver = webdriver.Chrome(
        service=Service(
            r"D:/TESTING/Automation/Github_repo/QA-Auto-project/chromedriver.exe")
    )

    # open https://github.com/login
    driver.get("https://github.com/login")

    # find neccesary field
    login_elem = driver.find_element(By.ID, "login_field")

    # enter wrong user name
    login_elem.send_keys("marta.talover@fakemail.com")

    # find password field
    pass_elem = driver.find_element(By.ID, "password")

    # enter wrong password
    pass_elem.send_keys("123456")
    time.sleep(3)

    # find sign in button
    button_elem = driver.find_element(By.NAME, "commit")

    # click left button on mouse
    button_elem.click()

    # check page title
    assert driver.title == "Sign in to GitHub · GitHub"
    time.sleep(3)

    # close browser
    driver.close()
