#TODO NewPostPage
import os

from selenium.webdriver.common.by import By
from Elements.UserHeader import UserHeader
from Pages.BasePage import BasePage


class NewPostPageLocators:
    ADD_POST_FORM = (By.CLASS_NAME, "card")
    CHOOSE_PHOTO_FIELD = (By.ID, 'image')
    DESCRIPTION_FIELD = (By.ID, 'description')
    CREATE_BUTTON = (By.ID, "send")

    INVALID_FEEDBACK = (By.CLASS_NAME, 'invalid-feedback.d-inline')


class NewPostPage(BasePage):
    def __init__(self, driver, debug):
        super().__init__(driver, debug)
        self.header = UserHeader(driver, debug)

    def add_post(self, photo, description="#photo #test"):
        add_post_form = self.driver.find_element(*NewPostPageLocators.ADD_POST_FORM)
        photo_field = add_post_form.find_element(*NewPostPageLocators.CHOOSE_PHOTO_FIELD)
        description_field = add_post_form.find_element(*NewPostPageLocators.DESCRIPTION_FIELD)
        create_button = add_post_form.find_element(*NewPostPageLocators.CREATE_BUTTON)

        if len(photo) > 0: #problem z przekazywaniem path bez pliku na końcu
            if self.debug: print(os.getcwd().split('laragram-automated-tests')[0]+"laragram-automated-tests/fotos/"+photo)
            photo_field.send_keys(os.getcwd().split('laragram-automated-tests')[0]+"laragram-automated-tests/fotos/"+photo)
            if self.debug: print("Image path field filled")

        description_field.send_keys(description)
        if self.debug: print("Description field filled")

        create_button.click()
        if self.debug: print("Create post button clicked")

    def checkInvalidDataFeedback(self):
        self.driver.find_element(*NewPostPageLocators.INVALID_FEEDBACK)
        if self.debug: print("Invalid feedback found")
