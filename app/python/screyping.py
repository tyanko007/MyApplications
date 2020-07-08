# coding: utf-8

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time

# firefox headless mode exec
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)

url = "https://www.pixiv.net/tags/apple"
driver.get(url)
data = driver.page_source.encode("utf-8")
driver.close()

print(data)
