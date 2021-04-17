from selenium.webdriver.common.by import By
from Elements.BasicElement import BasicElement


class FeedPostLocators:
    POST_HEADER = (By.CLASS_NAME, "card-body.p-3")
    POST_HEADER_USER_IMAGE = (By.TAG_NAME, "img")
    POST_HEADER_USER_NAME = (By.TAG_NAME, "a")

    POST_IMAGE = (By.XPATH, "//*[@alt='Post image']")

    POST_FOOTER = (By.CLASS_NAME, "card-body.p-2.border-top")
    POST_FOOTER_COMMENT_BUTTON = (By.CSS_SELECTOR, "div:nth-child(1) > a:nth-child(2)")
    POST_FOOTER_USER_NAME = (By.CLASS_NAME, "card-body.p-2.border-top")


class FeedPost(BasicElement):
    def goToAddCommentPage(self):
        post_footer = self.driver.find_element(*FeedPostLocators.POST_FOOTER)
        add_comment_page_button = post_footer.find_element(*FeedPostLocators.POST_FOOTER_COMMENT_BUTTON)
        add_comment_page_button.click()
        if self.debug: print("Add comment button clicked")

    def goToUserProfilePage(self):
        post_header = self.driver.find_element(*FeedPostLocators.POST_HEADER)
        user_profile_button = post_header.find_element(*FeedPostLocators.POST_HEADER_USER_NAME)
        user_profile_button.click()
        if self.debug: print("POST_HEADER_USER_NAME link clicked")

