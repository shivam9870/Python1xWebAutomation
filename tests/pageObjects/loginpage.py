# Page Class -

# Page locators
# Page Actions
# Webdriver - Init
# Custom functions
# No assertion here

from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    # Page Locators
    username = (By.XPATH, "//input[@id='login-username']")
    password = (By.XPATH, "//input[@id='login-password']")
    submit = (By.XPATH, "//button[@id='js-login-btn']")
    error_message = (By.CSS_SELECTOR, "#js-notification-box-msg")

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit(self):
        return self.driver.find_element(*LoginPage.submit)

    def get_error_massage(self):
        return self.driver.find_element(*LoginPage.error_message)

    # Page Actions

    def login_to_vwo(self, user, pwd):
        self.get_username().send_keys(user)
        self.get_password().send_keys(pwd)
        self.get_submit().click()
