#TODO NewPostPage
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class NewPostPageLocators:
    ADD_POST_FORM = (By.CLASS_NAME, "card")
    CHOOSE_PHOTO_FIELD = (By.ID, 'image')
    DESCRIPTION_FIELD = (By.ID, 'description')
    CREATE_BUTTON = (By.ID, "send")


class NewPostPage(BasePage):
    def add_post(self, photo, description="super fotka <3 pozdrawiam"):
        pass