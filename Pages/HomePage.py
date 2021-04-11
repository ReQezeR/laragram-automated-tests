#TODO HomePage
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class HomePageLocators:
    SHARE_PHOTO_PAGE_LINK = (By.LINK_TEXT, "//*[@title='New post']")
    YOUR_PROFILE_PAGE_LINK = (By.LINK_TEXT, "//*[@title='Your Profile']")
    SETTINGS_PAGE_LINK = (By.LINK_TEXT, "//*[@title='Settings']")
    LOGOUT_LINK = (By.XPATH, "//*[@title='Logout']")


class HomePage(BasePage):
    def logout(self):
        logout_button = self.driver.find_element(*HomePageLocators.LOGOUT_LINK)
        logout_button.click()

    def go_to_share_photo_page(self):
        share_photo_button = self.driver.find_element(*HomePageLocators.SHARE_PHOTO_PAGE_LINK)
        share_photo_button.click()

    def go_to_settings_page(self):
        settings_button = self.driver.find_element(*HomePageLocators.SETTINGS_PAGE_LINK)
        settings_button.click()

    def go_to_profile_page(self):
        profile_button = self.driver.find_element(*HomePageLocators.YOUR_PROFILE_PAGE_LINK)
        profile_button.click()
