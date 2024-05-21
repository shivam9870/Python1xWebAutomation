# Page Locators
# Page Actions
from selenium.webdriver.common.by import By
# Page Class
class Dashboard_page():
    def __int__(self, driver):
        self.driver = driver

    user_logged_in = (By.CLASS_NAME,"//span[@class='Fw(semi-bold) ng-binding']")

    def get_user_logged_in(self):
        return self.driver.find_element(*Dashboard_page.user_logged_in)

    def userlogged_inText(self):
        return self.get_user_logged_in().text()