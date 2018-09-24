import requests
import contextlib
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
import time
import lxml.html as LH
import lxml.html.clean as clean
import nltk
import os

def checkOp(op):
    if (op.isdigit()):
        op = int(op)
        if (op>0 and op<8):
            return True
    return False

pais = "us"
url="https://github.com/search"
browser = webdriver.Chrome("C:\\Users\\Carlo Orellana\\Downloads\\chromedriver.exe") #chromedriver.exe location
browser.get(url)  # Load page

msg_box = browser.find_element_by_name("q")
msg_box.click()
msg_box.send_keys("location:"+pais+"\n")

nUsers = browser.find_element_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div/div[1]/h3')
nUsers = nUsers.text.split(" ")[0]
nUsers = int(nUsers.replace(',', ''))

