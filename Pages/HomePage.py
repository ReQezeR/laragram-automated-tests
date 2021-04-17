import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Elements.FeedPost import FeedPost
from Elements.UserHeader import UserHeader
from Pages.BasePage import BasePage


class HomePageLocators:
    FEED_POSTS = (By.CLASS_NAME, 'col-12.col-md-8')
    FEED_POST = (By.CLASS_NAME, 'card.mb-2')
    LOGGED_USER_NAME = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div[2]/a')


class HomePage(BasePage):
    def __init__(self, driver, debug):
        super().__init__(driver, debug)
        self.header = UserHeader(driver, debug)

    def goToRandomPostFromFeed(self):
        feed = self.driver.find_element(*HomePageLocators.FEED_POSTS)
        post_list = feed.find_elements(*HomePageLocators.FEED_POST)
        assert len(post_list) != 0
        feed_post = FeedPost(random.choice(post_list), debug=self.debug) # wybranie losowego postu
        feed_post.goToAddCommentPage()

    def checkUser(self, login):
        userName = self.driver.find_element(*HomePageLocators.LOGGED_USER_NAME)
        assert (userName.text == login)

