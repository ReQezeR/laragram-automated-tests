#TODO MainPage
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class MainPageLocators:
    REGISTER_FORM = (By.CLASS_NAME, "card")
    NAME_FIELD = (By.ID, 'name')
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'password')
    PASSWORD_CONFIRM_FIELD = (By.ID, 'password-confirm')
    REGISTER_BUTTON = (By.TAG_NAME, "button")

    LOGIN_PAGE_LINK = (By.LINK_TEXT, "Login")
    REGISTER_PAGE_LINK = (By.LINK_TEXT, "Register")


class MainPage(BasePage):
    def register(self, username="Abadozaur123", email="Abadozaur@gmail.com", password="testtest123"):
        register_form = self.driver.find_element(*MainPageLocators.REGISTER_FORM)
        name_field = register_form.find_element(*MainPageLocators.NAME_FIELD)
        email_field = register_form.find_element(*MainPageLocators.EMAIL_FIELD)
        password_field = register_form.find_element(*MainPageLocators.PASSWORD_FIELD)
        password2_field = register_form.find_element(*MainPageLocators.PASSWORD_CONFIRM_FIELD)
        register_confirm_button = register_form.find_element(*MainPageLocators.REGISTER_BUTTON)

        name_field.send_keys(username)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password2_field.send_keys(password)
        register_confirm_button.click()

    def go_to_login_page(self):
        # assert "A simplified clone of instagram created with" not in self.driver.page_source
        login_page_button = self.driver.find_element(*MainPageLocators.LOGIN_PAGE_LINK)
        login_page_button.click()
