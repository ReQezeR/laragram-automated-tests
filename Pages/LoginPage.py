#TODO LoginPage
from selenium.webdriver.common.by import By
from BasePage import BasePage


class LoginPageLocators:
    EXAMPLE_LOCATOR = (By.CLASS_NAME, 'css-34e4ux')


class LoginPage(BasePage):
    def login(self):
        pass