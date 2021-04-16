from selenium.webdriver.common.by import By
from Elements.BasicHeader import BasicHeader
from Pages.BasePage import BasePage


class LoginPageLocators:
    LOGIN_FORM = (By.CLASS_NAME, "card")
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.TAG_NAME, "button")

    INVALID_FEEDBACK = (By.CLASS_NAME, "invalid-feedback")


class LoginPage(BasePage):
    def __init__(self, driver, debug):
        super().__init__(driver, debug)
        self.header = BasicHeader(driver, debug)

    def login(self, email="mp62639@o2.pl", password="admin123"):
        login_form = self.driver.find_element(*LoginPageLocators.LOGIN_FORM)
        email_field = login_form.find_element(*LoginPageLocators.EMAIL_FIELD)
        password_field = login_form.find_element(*LoginPageLocators.PASSWORD_FIELD)
        login_confirm_button = login_form.find_element(*LoginPageLocators.LOGIN_BUTTON)
        email_field.send_keys(email)
        if self.debug: print("Email field filled")

        password_field.send_keys(password)
        if self.debug: print("Password field filled")

        login_confirm_button.click()
        if self.debug: print("Login button clicked")

    def checkInvalidDataFeedback(self):
        self.driver.find_element(*LoginPageLocators.INVALID_FEEDBACK)
        if self.debug: print("Invalid feedback found")
