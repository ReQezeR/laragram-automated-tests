#TODO NewPostPage
import os

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class NewPostPageLocators:
    ADD_POST_FORM = (By.CLASS_NAME, "card")
    CHOOSE_PHOTO_FIELD = (By.ID, 'image')
    DESCRIPTION_FIELD = (By.ID, 'description')
    CREATE_BUTTON = (By.ID, "send")


class NewPostPage(BasePage):
    def add_post(self, photo, description="super fotka"):
        add_post_form = self.driver.find_element(*NewPostPageLocators.ADD_POST_FORM)

        photo_field = add_post_form.find_element(*NewPostPageLocators.CHOOSE_PHOTO_FIELD)
        description_field = add_post_form.find_element(*NewPostPageLocators.DESCRIPTION_FIELD)
        create_button = add_post_form.find_element(*NewPostPageLocators.CREATE_BUTTON)

        print(os.getcwd()+"/fotos/"+photo)
        photo_field.send_keys(os.getcwd()+"/fotos/"+photo)
        description_field.send_keys(description)
        create_button.click()