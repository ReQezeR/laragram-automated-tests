import time
from selenium import webdriver
import unittest
from Pages.HomePage import HomePage
from Pages.MainPage import MainPage
from Pages.RegisterPage import RegisterPage


class RegisterTest(unittest.TestCase):
    debug = False

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("-incognito")
        options.add_argument('headless')
        cls.driver = webdriver.Chrome("../drivers/chromedriver", options=options)
        cls.driver.implicitly_wait(5)

    def test_main_page_register_with_good_data(self, login="registerTest", email="registerTest@testowo.com", password="TestTest123"):
        now = str(time.time())
        login = login+now
        email = login+now+"@testowo.com"
        driver = self.driver
        driver.get("http://laragram.ml/")
        mainPage = MainPage(driver, debug=self.debug)
        mainPage.register_form.register(username=login, email=email, password=password)
        homePage = HomePage(driver, debug=self.debug)
        homePage.checkUser(login)
        homePage.header.logout()

    def test_main_page_register_with_wrong_data(self, login="agent00", email="agent00@testowo.com", password="TestTest123"):
        driver = self.driver
        driver.get("http://laragram.ml/")
        mainPage = MainPage(driver, debug=self.debug)
        mainPage.register_form.register(username=login, email=email, password=password)
        mainPage.register_form.checkInvalidDataFeedback()

    def test_register_page_register_with_good_data(self, login="registerTest", email="registerTest@testowo.com", password="TestTest123"):
        now = str(time.time())
        login = login + now
        email = login + now + "@testowo.com"
        driver = self.driver
        driver.get("http://laragram.ml/")
        mainPage = MainPage(driver, debug=self.debug)
        mainPage.header.go_to_register_page()
        registerPage = RegisterPage(driver, debug=self.debug)
        registerPage.register_form.register(username=login, email=email, password=password)
        homePage = HomePage(driver, debug=self.debug)
        homePage.checkUser(login)
        homePage.header.logout()

    def test_register_page_register_with_wrong_data(self, login="agent00", email="agent00@testowo.com", password="TestTest123"):
        driver = self.driver
        driver.get("http://laragram.ml/")
        mainPage = MainPage(driver, debug=self.debug)
        mainPage.header.go_to_register_page()
        registerPage = RegisterPage(driver, debug=self.debug)
        registerPage.register_form.register(username=login, email=email, password=password)
        registerPage.register_form.checkInvalidDataFeedback()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
