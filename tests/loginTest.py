from selenium import webdriver
import unittest

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage


class LoginTest(unittest.TestCase):
    debug = False

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("-incognito")
        options.add_argument('headless')
        cls.driver = webdriver.Chrome("../drivers/chromedriver", options=options)
        cls.driver.implicitly_wait(5)

    def test_login_with_good_data(self, login="agent00", email="agent00@testowo.com", password="TestTest123"):
        driver = self.driver
        driver.get("http://laragram.ml/")
        mainPage = MainPage(driver, debug=self.debug)
        mainPage.header.go_to_login_page()
        loginPage = LoginPage(driver, debug=self.debug)
        loginPage.login(email, password)
        homePage = HomePage(driver, debug=self.debug)
        homePage.checkUser(login) #sprawdzenie czy poprawnie zalogowano
        homePage.header.logout()

    def test_login_with_wrong_data(self, login="brak", email="brak@brak.com", password="TestTest123"):
        driver = self.driver
        driver.get("http://laragram.ml/")
        mainPage = MainPage(driver, debug=self.debug)
        mainPage.header.go_to_login_page()
        loginPage = LoginPage(driver, debug=self.debug)
        loginPage.login(email, password)
        loginPage.checkInvalidDataFeedback() #sprawdzenie czy nie zalogowano

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
