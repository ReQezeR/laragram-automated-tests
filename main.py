from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage


def login_user(driver):
    driver.get("http://laragram.ml/")
    mainPage = MainPage(driver, debug=False)
    mainPage.register()


def register_user(driver):
    driver.get("http://laragram.ml/")
    mainPage = MainPage(driver, debug=False)
    mainPage.go_to_login_page()
    loginPage = LoginPage(driver, debug=False)
    loginPage.login()


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("-incognito")
    # options.add_argument('headless')

    driver = webdriver.Chrome("./drivers/chromedriver", options=options)
    
    driver.close()
