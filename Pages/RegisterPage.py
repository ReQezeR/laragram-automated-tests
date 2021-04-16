from selenium.webdriver.common.by import By
from Elements.BasicHeader import BasicHeader
from Elements.RegisterForm import RegisterForm
from Pages.BasePage import BasePage


class RegisterPageLocators:
    EXAMPLE_LOCATOR = (By.CLASS_NAME, 'css-34e4ux')


class RegisterPage(BasePage):
    def __init__(self, driver, debug):
        super().__init__(driver, debug)
        self.header = BasicHeader(driver, debug)
        self.register_form = RegisterForm(driver, debug)