from random import randint
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
from Pages.NewPostPage import NewPostPage


def register_user(driver, username, email, password):
    driver.get("http://laragram.ml/")
    mainPage = MainPage(driver, debug=False)
    mainPage.register(username, email, password)
    homePage = HomePage(driver, debug=False)
    homePage.logout()


def login_user(driver, username, password):
    driver.get("http://laragram.ml/")
    mainPage = MainPage(driver, debug=False)
    mainPage.go_to_login_page()
    loginPage = LoginPage(driver, debug=False)
    loginPage.login(username, password)


def populate_accounts(driver, count):
    for i in range(count):
        register_user(driver, username="agent0"+str(i), email="agent0"+str(i)+"@testowo.com", password="TestTest123")
        print(i)


def populate_photos(driver, acount_number, photo_count):
    for i in range(acount_number):
        login_user(driver, username="agent0"+str(i), password="TestTest123")
        print(i)
        # login_user(driver, username="mp62639@o2.pl", password="admin123")
        homePage = HomePage(driver, debug=False)
        for j in range(photo_count):
            photo_id = str(randint(1, 25))+".jpg"
            homePage.go_to_share_photo_page()

            newPostPage = NewPostPage(driver, debug=False)
            newPostPage.add_post(photo=photo_id, description="#fotka #przyjazn #life #cool")
        homePage.logout()


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("-incognito")
    options.add_argument('headless')

    driver = webdriver.Chrome("./drivers/chromedriver", options=options)
    # populate_accounts(driver, 10)
    populate_photos(driver, 10, 13)
    # sleep(10)
    driver.close()
