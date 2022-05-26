

import requests as req
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time

# path = "C:\webdrivers\chromedriver.exe"

# browser = webdriver.Chrome(path)
# browser.get("https://th.kerryexpress.com/th/track/")
# time.sleep(7)
# key = browser.find_element_by_xpath('/html/body/kett-root/kett-search-form/div/div/div/form/div/div[1]/input')
# key.send_keys('SNDA000211340')
# time.sleep(1)
# submit = browser.find_element_by_xpath('/html/body/kett-root/kett-search-form/div/div/div/form/div/div[2]/button')
# time.sleep(1)
# submit.click()

def check():
    url = 'https://th.kerryexpress.com/th/track/?track=OTExMGJhN2I2NmRjYWI1MzQ5NzBlMTVlZWFiMWY4ZmFmSHg4ZTIxZmFhZTMyMTJkYzI0NDNlZTk4OWUyZGU3MzZjYjlmSHg4VE5LUzAwMDAxNDE0M05OZkh4ODIzNzA2NDRiODBjNjAxYjJmZGZmZTE2MzY5ZmVlOTIwZkh4ODRjNDE0YTUyZmQ4ODMyZGY5ZjA2ZWY3ZjdmYzIzYTk3'
    rawdata = req.get(url)
    rawdata = rawdata.content
    data = BeautifulSoup(rawdata,'html.parser')
    find = data.find_all('span')
    print(find)
    # for i in find:
    #     print(i.text)


#     return find


# use = check()

# print(use)

check()