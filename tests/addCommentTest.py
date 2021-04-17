from selenium import webdriver
import time
import unittest

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from Pages.PostPage import PostPage


class AddCommentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("-incognito")
        options.add_argument('headless')
        cls.driver = webdriver.Chrome("../drivers/chromedriver", options=options)
        cls.driver.implicitly_wait(5)

    def test_add_comment(self, email="agent00@testowo.com", password="TestTest123"):
        debug = False
        driver = self.driver
        driver.get("http://laragram.ml/")
        mainPage = MainPage(driver, debug=debug)
        mainPage.header.go_to_login_page()
        loginPage = LoginPage(driver, debug=debug)
        loginPage.login(email, password)
        homePage = HomePage(driver, debug=debug)
        homePage.goToRandomPostFromFeed()
        postPage = PostPage(driver, debug=debug)
        postPage.addComment("Nice one!")
        postPage.checkComment("Nice one!")
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
