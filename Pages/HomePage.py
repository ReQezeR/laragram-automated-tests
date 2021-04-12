#TODO HomePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Pages.BasePage import BasePage


class HomePageLocators:
    SHARE_PHOTO_PAGE_LINK = (By.XPATH, "//*[@title='New post']")
    YOUR_PROFILE_PAGE_LINK = (By.XPATH, "//*[@title='Your Profile']")
    SETTINGS_PAGE_LINK = (By.XPATH, "//*[@title='Settings']")
    LOGOUT_LINK = (By.XPATH, "//*[@title='Logout']")


class HomePage(BasePage):
    def logout(self):
        logout_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(HomePageLocators.LOGOUT_LINK))
        # logout_button = self.driver.find_element(*HomePageLocators.LOGOUT_LINK)
        logout_button.click()

    def go_to_share_photo_page(self):
        share_photo_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(HomePageLocators.SHARE_PHOTO_PAGE_LINK))
        # share_photo_button = self.driver.find_element(*HomePageLocators.SHARE_PHOTO_PAGE_LINK)
        share_photo_button.click()

    def go_to_settings_page(self):
        settings_button = self.driver.find_element(*HomePageLocators.SETTINGS_PAGE_LINK)
        settings_button.click()

    def go_to_profile_page(self):
        profile_button = self.driver.find_element(*HomePageLocators.YOUR_PROFILE_PAGE_LINK)
        profile_button.click()
