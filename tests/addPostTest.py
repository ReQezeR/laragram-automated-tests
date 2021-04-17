from random import randint

from selenium import webdriver
import time
import unittest

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from Pages.NewPostPage import NewPostPage
from Pages.PostPage import PostPage


class AddPostTest(unittest.TestCase):
    debug = False

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("-incognito")
        options.add_argument('headless')
        cls.driver = webdriver.Chrome("../drivers/chromedriver", options=options)
        cls.driver.implicitly_wait(10)

    def test_add_post_with_good_data(self, email="agent01@testowo.com", password="TestTest123", photo="", description="#add_post_test"):
        photo = str(randint(1, 25))+".jpg"
        description = str(time.time())+" "+description
        driver = self.driver
        driver.get("http://laragram.ml/")
        mainPage = MainPage(driver, debug=self.debug)
        mainPage.header.goToLoginPage()
        loginPage = LoginPage(driver, debug=self.debug)
        loginPage.login(email, password)
        homePage = HomePage(driver, debug=self.debug)
        homePage.header.goToNewPostPage()
        newPostPage = NewPostPage(driver, debug=self.debug)
        newPostPage.add_post(photo=photo, description=description)
        postPage = PostPage(driver, debug=self.debug)
        postPage.checkDescription(description)
        postPage.header.logout()

    def test_add_post_with_wrong_data(self, email="agent00@testowo.com", password="TestTest123", photo="", description="#add_post_test"):
        description = str(time.time()) + " " + description
        driver = self.driver
        driver.get("http://laragram.ml/")
        mainPage = MainPage(driver, debug=self.debug)
        mainPage.header.goToLoginPage()
        loginPage = LoginPage(driver, debug=self.debug)
        loginPage.login(email, password)
        homePage = HomePage(driver, debug=self.debug)
        homePage.header.goToNewPostPage()
        newPostPage = NewPostPage(driver, debug=self.debug)
        newPostPage.add_post(photo=photo, description=description)
        newPostPage.checkInvalidDataFeedback()
        newPostPage.header.logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
