import re
import requests
import time
import random
import os
from bs4 import BeautifulSoup
from selenium import webdriver

os.chdir("C:\\Users\\anass\\Desktop\\linkedin")

def connection(link):
    browser = webdriver.Chrome()
    browser.get(link)
    try:
        file = open('config.txt')
        lines = file.readlines()
        username = lines[0]
        password = lines[1]
    except NameError:
        print("config.txt is not define")
    except IndexError:
        print("username or password is not found")
        
    elementID = browser.find_element_by_id('username')
    elementID.send_keys(username)

    elementID = browser.find_element_by_id('password')
    elementID.send_keys(password)

    elementID.submit()

    return browser

def collection(browser):

    SCROLL_PAUSE_TIME = 6
    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    for i in range(1000):
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    src = browser.page_source
    try:
        soup = BeautifulSoup(src, 'lxml')
    except:
        print("lxml is not installed")
    #soup
    name_div = soup.findAll('div', {'class': 'relative ember-view'})
    return(name_div)


