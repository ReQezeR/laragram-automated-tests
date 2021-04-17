from selenium.webdriver.common.by import By
from Elements.BasicHeader import BasicHeader
from Elements.UserHeader import UserHeader
from Pages.BasePage import BasePage


class SearchResultPageLocators:
    RESULT_LIST = (By.CLASS_NAME, 'list-group')
    SINGLE_RESULT = (By.CLASS_NAME, 'list-group-item')
    SINGLE_RESULT_LINK = (By.CLASS_NAME, 'text-dark.font-weight-bold')

    NO_RESULTS = (By.CLASS_NAME, 'text-muted')


class SearchResultPage(BasePage):
    def __init__(self, driver, debug, userSession=False):
        super().__init__(driver, debug)
        if userSession:
            self.header = UserHeader(driver, debug)
        else:
            self.header = BasicHeader(driver, debug)

    def findSearchQuery(self, query):
        result_list = self.driver.find_element(*SearchResultPageLocators.RESULT_LIST)
        assert query in result_list.text

    def checkNoResult(self):
        self.driver.find_element(*SearchResultPageLocators.NO_RESULTS)
        if self.debug: print("No result found")
