from selenium.webdriver.common.by import By
from Elements.BasicElement import BasicElement


class RegisterFormLocators:
    REGISTER_FORM = (By.CLASS_NAME, "card")
    NAME_FIELD = (By.ID, 'name')
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'password')
    PASSWORD_CONFIRM_FIELD = (By.ID, 'password-confirm')
    REGISTER_BUTTON = (By.TAG_NAME, "button")

    INVALID_FEEDBACK = (By.CLASS_NAME, "invalid-feedback")


class RegisterForm(BasicElement):
    def register(self, username="Abadozaur123", email="Abadozaur@gmail.com", password="testtest123"):
        register_form = self.driver.find_element(*RegisterFormLocators.REGISTER_FORM)
        name_field = register_form.find_element(*RegisterFormLocators.NAME_FIELD)
        email_field = register_form.find_element(*RegisterFormLocators.EMAIL_FIELD)
        password_field = register_form.find_element(*RegisterFormLocators.PASSWORD_FIELD)
        password2_field = register_form.find_element(*RegisterFormLocators.PASSWORD_CONFIRM_FIELD)
        register_confirm_button = register_form.find_element(*RegisterFormLocators.REGISTER_BUTTON)

        name_field.send_keys(username)
        if self.debug: print("Username field filled")

        email_field.send_keys(email)
        if self.debug: print("Email field filled")

        password_field.send_keys(password)
        if self.debug: print("Password field filled")

        password2_field.send_keys(password)
        if self.debug: print("Confirm password field filled")

        register_confirm_button.click()
        if self.debug: print("Register button clicked")

    def checkInvalidDataFeedback(self):
        self.driver.find_element(*RegisterFormLocators.INVALID_FEEDBACK)
        if self.debug: print("Invalid feedback found")
