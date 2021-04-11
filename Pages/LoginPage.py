#TODO LoginPage
from time import sleep

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class LoginPageLocators:
    LOGIN_FORM = (By.CLASS_NAME, "card")
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.TAG_NAME, "button")

    LOGIN_PAGE_LINK = (By.LINK_TEXT, "Login")
    REGISTER_PAGE_LINK = (By.LINK_TEXT, "Register")


class LoginPage(BasePage):
    def login(self):
        login_form = self.driver.find_element(*LoginPageLocators.LOGIN_FORM)
        email_field = login_form.find_element(*LoginPageLocators.EMAIL_FIELD)
        password_field = login_form.find_element(*LoginPageLocators.PASSWORD_FIELD)
        login_confirm_button = login_form.find_element(*LoginPageLocators.LOGIN_BUTTON)

        email_field.send_keys("mp62639@o2.pl")
        password_field.send_keys("admin123")
        login_confirm_button.click()
        sleep(20)