import time
from selenium.webdriver.common.by import By
from Elements.UserHeader import UserHeader
from Pages.BasePage import BasePage


class PostPageLocators:
    COMMENT_SECTION = (By.CLASS_NAME, 'list-unstyled.m-0')
    COMMENT = (By.TAG_NAME, "span")

    COMMENT_FORM = (By.ID, 'comment-form')
    COMMENT_INPUT = (By.ID, 'comment')
    COMMENT_SUBMIT_BUTTON = (By.TAG_NAME, 'button')


class PostPage(BasePage):
    def __init__(self, driver, debug):
        super().__init__(driver, debug)
        self.header = UserHeader(driver, debug)

    def addComment(self, value):
        comment_form = self.driver.find_element(*PostPageLocators.COMMENT_FORM)
        comment_input = comment_form.find_element(*PostPageLocators.COMMENT_INPUT)
        comment_submit_button = comment_form.find_element(*PostPageLocators.COMMENT_SUBMIT_BUTTON)
        comment_input.send_keys(value)
        if self.debug: print("Comment input filled: {}".format(value))
        comment_submit_button.click()
        if self.debug: print("Add comment button clicked")

    def checkComment(self, value):
        time.sleep(2)
        comment_section = self.driver.find_element(*PostPageLocators.COMMENT_SECTION)
        comments = comment_section.find_elements(*PostPageLocators.COMMENT)
        check_flag = False
        for c in comments:
            if value in c.text:
                check_flag = True
                if self.debug: print("Comment found")
                break
        assert check_flag

    def checkDescription(self, query):
        comment_section = self.driver.find_element(*PostPageLocators.COMMENT_SECTION)
        comments = comment_section.find_elements(*PostPageLocators.COMMENT)
        check_flag = False
        for c in comments:
            if query in c.text:
                check_flag = True
                if self.debug: print("Description found")
                break
        assert check_flag

