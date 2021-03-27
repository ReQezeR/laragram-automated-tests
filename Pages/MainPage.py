#TODO MainPage
from selenium.webdriver.common.by import By
from BasePage import BasePage


class MainPageLocators:
    EXAMPLE_LOCATOR = (By.CLASS_NAME, 'css-34e4ux')


class MainPage(BasePage):
    def register(self):
        pass

    def go_to_login_page(self):
        pass