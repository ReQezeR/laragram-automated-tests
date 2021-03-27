#TODO RegisterPage
from selenium.webdriver.common.by import By
from BasePage import BasePage


class RegisterPageLocators:
    EXAMPLE_LOCATOR = (By.CLASS_NAME, 'css-34e4ux')


class RegisterPage(BasePage):
    def register(self):
        pass