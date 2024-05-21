# Assertion here
import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.pageObjects.loginpage import LoginPage
from tests.pageObjects.dashboardPage import Dashboard_page
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



# start the webdriver
# call the page object
# verify the logic

@pytest.fixture()
def setup1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    yield driver
    driver.quit()

@allure.epic("VWO Login Test")
@allure.feature("TC#1 - VWO App Positive Testcase")
def test_vwoLogin(setup1):
    driver = setup1
    loginpage = LoginPage(driver)

    # Wait for the username input field to be visible
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='login-username']")))

    loginpage.login_to_vwo(user="relaxeddirac4@justzeus.com", pwd="ATBx@1234")
    time.sleep(5)

    assert "Dashboard" in driver.title
    time.sleep(2)
