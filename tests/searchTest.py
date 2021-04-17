import time

from selenium import webdriver
import unittest
from Pages.MainPage import MainPage
from Pages.SearchResultPage import SearchResultPage


class SearchTest(unittest.TestCase):
    debug = False

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("-incognito")
        options.add_argument('headless')
        cls.driver = webdriver.Chrome("../drivers/chromedriver", options=options)
        cls.driver.implicitly_wait(5)

    def test_search_with_good_data(self, query="agent00"):
        driver = self.driver
        driver.get("http://laragram.ml/")
        mainPage = MainPage(driver, debug=self.debug)
        mainPage.header.search(query)
        searchResultPage = SearchResultPage(driver, debug=self.debug, userSession=False)
        searchResultPage.findSearchQuery(query=query)

    def test_search_with_wrong_data(self, query="brak"):
        driver = self.driver
        driver.get("http://laragram.ml/")
        mainPage = MainPage(driver, debug=self.debug)
        mainPage.header.search(query)
        searchResultPage = SearchResultPage(driver, debug=self.debug, userSession=False)
        searchResultPage.checkNoResult()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
