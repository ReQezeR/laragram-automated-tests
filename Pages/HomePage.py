#TODO HomePage
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class HomePageLocators:
    EXAMPLE_LOCATOR = (By.CLASS_NAME, 'css-34e4ux')


class HomePage(BasePage):
    pass