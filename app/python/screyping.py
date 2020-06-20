# coding: utf-8

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

# firefox headless mode exec
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)

url = "https://www.pixiv.net"
driver.get(url)
data = driver.page_source.encode("utf-8")

# login button push
signin = driver.find_element_by_class_name("signup-form__submit--login")
signin.click()

# login email & password args
print(url + "へログインするための情報を入力してください")
#email = input("ログインEmail　>>")
#password = input("ログインパスワード >>")

#soup = BeautifulSoup(data, features="html.parser")
#email_form = soup.find("div", class_="input-field")
email_input = driver.find_elements_by_tag_name("input")
print email_input
