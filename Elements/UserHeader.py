from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Elements.BasicElement import BasicElement


class UserHeaderLocators:
    HOME_PAGE_LINK = (By.CLASS_NAME, "navbar-brand")
    SEARCH_FORM = (By.CLASS_NAME, "form-inline")
    SEARCH_FIELD = (By.TAG_NAME, "input")
    SEARCH_BUTTON = (By.TAG_NAME, "button")

    NEW_POST_PAGE_LINK = (By.XPATH, "//*[@title='New post']")
    YOUR_PROFILE_PAGE_LINK = (By.XPATH, "//*[@title='Your Profile']")
    SETTINGS_PAGE_LINK = (By.XPATH, "//*[@title='Settings']")
    LOGOUT_LINK = (By.XPATH, "//*[@title='Logout']")


class UserHeader(BasicElement):
    def search(self, query):
        search_form = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UserHeaderLocators.SEARCH_FORM))
        search_input = search_form.find_element(*UserHeaderLocators.SEARCH_FIELD)
        search_button = search_form.find_element(*UserHeaderLocators.SEARCH_BUTTON)
        search_input.send_keys(query)
        if self.debug: print("Search input filled: {}".format(query))
        search_button.click()
        if self.debug: print("Search button clicked")

    def go_to_home_page(self):
        home_page_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UserHeaderLocators.HOME_PAGE_LINK))
        home_page_button.click()
        if self.debug: print("HomePage button clicked")

    def logout(self):
        logout_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UserHeaderLocators.LOGOUT_LINK))
        logout_button.click()
        if self.debug: print("Logout button clicked")

    def go_to_new_post_page(self):
        new_post_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UserHeaderLocators.NEW_POST_PAGE_LINK))
        new_post_button.click()
        if self.debug: print("NewPostPage button clicked")

    def go_to_settings_page(self):
        settings_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UserHeaderLocators.SETTINGS_PAGE_LINK))
        settings_button.click()
        if self.debug: print("Settings button clicked")

    def go_to_your_profile_page(self):
        your_profile_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(UserHeaderLocators.YOUR_PROFILE_PAGE_LINK))
        your_profile_button.click()
        if self.debug: print("YourProfile button clicked")
