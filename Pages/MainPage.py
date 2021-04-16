from selenium.webdriver.common.by import By
from Elements.BasicHeader import BasicHeader
from Elements.RegisterForm import RegisterForm
from Pages.BasePage import BasePage


class MainPageLocators:
    pass


class MainPage(BasePage):
    def __init__(self, driver, debug):
        super().__init__(driver, debug)
        self.header = BasicHeader(driver, debug)
        self.register_form = RegisterForm(driver, debug)