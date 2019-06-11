# -*- coding: utf-8 -*-
"""
爬取網頁的食物資料
"""
#from selenium import webdriver
from selenium import webdriver
from bs4 import BeautifulSoup
import re

food_name = "rice"
driver = webdriver.Chrome("C:\\Users\\User\\chromedriver.exe")
driver.get("http://www.glycemicindex.com/foodSearch.php")
driver.find_element_by_name("food_name").click()
driver.find_element_by_name("food_name").clear()
driver.find_element_by_name("food_name").send_keys(food_name)
driver.find_element_by_name("find").click()

html = driver.page_source
soup = BeautifulSoup(html, features='lxml')
print(soup.find('a',{"href":re.compile("rice, white")}))#print table 為h1的內容
