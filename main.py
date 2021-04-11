from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage


def register_user(driver, username, email, password):
    driver.get("http://laragram.ml/")
    mainPage = MainPage(driver, debug=False)
    mainPage.register(username, email, password)
    homePage = HomePage(driver, debug=False)
    homePage.logout()


def login_user(driver):
    driver.get("http://laragram.ml/")
    mainPage = MainPage(driver, debug=False)
    mainPage.go_to_login_page()
    loginPage = LoginPage(driver, debug=False)
    loginPage.login()


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("-incognito")
    options.add_argument('headless')

    driver = webdriver.Chrome("./drivers/chromedriver", options=options)
    # for i in range(100):
    #     register_user(driver, username="testowy"+str(i), email="testowy"+str(i)+"@testowo.com", password="TestTest123")
    #     print(i)

    sleep(10)
    driver.close()
