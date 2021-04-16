from selenium.webdriver.common.by import By
from Elements.BasicElement import BasicElement


class BasicHeaderLocators:
    MAIN_PAGE_LINK = (By.CLASS_NAME, "navbar-brand")
    SEARCH_FORM = (By.CLASS_NAME, "form-inline")
    SEARCH_FIELD = (By.TAG_NAME, "input")
    SEARCH_BUTTON = (By.TAG_NAME, "button")
    LOGIN_PAGE_LINK = (By.LINK_TEXT, "Login")
    REGISTER_PAGE_LINK = (By.LINK_TEXT, "Register")


class BasicHeader(BasicElement):
    def search(self, query):
        search_form = self.driver.find_element(*BasicHeaderLocators.SEARCH_FORM)
        search_input = search_form.find_element(*BasicHeaderLocators.SEARCH_FIELD)
        search_button = search_form.find_element(*BasicHeaderLocators.SEARCH_BUTTON)
        search_input.send_keys(query)
        if self.debug: print("Search input filled: {}".format(query))
        search_button.click()
        if self.debug: print("Search button clicked")

    def go_to_home_page(self):
        main_page_button = self.driver.find_element(*BasicHeaderLocators.MAIN_PAGE_LINK)
        main_page_button.click()
        if self.debug: print("MainPage button clicked")

    def go_to_login_page(self):
        login_page_button = self.driver.find_element(*BasicHeaderLocators.LOGIN_PAGE_LINK)
        login_page_button.click()
        if self.debug: print("LoginPage button clicked")

    def go_to_register_page(self):
        register_page_button = self.driver.find_element(*BasicHeaderLocators.REGISTER_PAGE_LINK)
        register_page_button.click()
        if self.debug: print("RegisterPage button clicked")
