# coding: utf-8

# require packages
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

# webdriver run firefox headless
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)

# variable define
url = "https://www.pixiv.net" # pixivにログイン

## login def
def login(domain, username, password):
    driver.get(domain) # pixのログイン画面表示
    driver.find_element_by_class_name("signup-form__submit--login").click()
    time.sleep(2)
    fname = driver.find_element_by_name("input")
