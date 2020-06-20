# coding: utf-8

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJs()
driver.get("http://localhost/")

data = driver.page_source.encode("utf-8")

print(data)

# bs4 = BeautifulSoup(driver.page_source, "html5lib")

driver.find_element_by_name("name").send_keys("admin")
driver.find_element_by_name("pass").send_keys("amdin")
driver.find_element_by_name("login").click()

print(data)
