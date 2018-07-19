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

def getWordsHtml(url,archivo):
    browser = webdriver.Chrome("C:\\Users\\Carlo Orellana\\Downloads\\chromedriver.exe")
    ignore_tags = ('script', 'noscript', 'style')
    browser.get(url)  # Load page
    content = browser.page_source
    cleaner = clean.Cleaner()
    content = cleaner.clean_html(content)
    # open('source.html', 'w') as f:
    #    f.write(content.encode('utf-8'))
    doc = LH.fromstring(content)
    with open(archivo, 'w') as f:
        for elt in doc.iterdescendants():
            if elt.tag in ignore_tags: continue
            text = elt.text or ''
            tail = elt.tail or ''
            words = ' '.join((text, tail)).strip()
            if words:
                words = words.encode('utf-8')
                f.write(words.decode("utf-8") + '\n')
    browser.close()

year = '2017'
if not os.path.exists(year):
    os.makedirs(year)

url="https://scholar.google.com/scholar?hl=es&as_sdt=0%2C5&q=programming+language&btnG=&oq=programming+"
browser = webdriver.Chrome("C:\\Users\\Carlo Orellana\\Downloads\\chromedriver.exe")
browser.get(url)  # Load page
input("Resuelva los captchas (si los hubiese), deseleccione citas y patentes y presione enter para comenzar ")

isPresent = len(browser.find_elements_by_xpath('//*[@id="gs_n"]/center/table/tbody/tr/td[12]/a')) >0
i = 1
file = open(year+"/links.txt",'a')
while (isPresent):
    j = 1
    paperUrl = browser.find_elements_by_class_name('gs_rt')
    print("Pagina " + str(i))
    for paper in paperUrl:
        link = paper.find_element_by_tag_name('a')
        link = link.get_attribute('href')
        #r = requests.get(link)
        #content_type = r.headers.get('content-type')
        #if 'application/pdf' in content_type:
        #    ext = '.pdf'
        #if 'text/html' in content_type:
        #    getWordsHtml(link, year + "/" + str(i) + "-" + str(j) + ".txt")
        file.write(link + '\n')
        #else:
        #    ext = ''
        #    print('Unknown type: {}'.format(content_type))
        #time.sleep(1)
    user = browser.find_element_by_xpath('//*[@id="gs_n"]/center/table/tbody/tr/td[12]/a')
    user.click()
    time.sleep(2)
    isPresent = len(browser.find_elements_by_xpath('//*[@id="gs_n"]/center/table/tbody/tr/td[12]/a')) > 0
    i+=1
    if (isPresent == False):
        print("1. Captcha\n2. Fin de busqueda")
        op = int(input("Seleccione lo ocurrido: "))
        if (op == 1):
            isPresent == True
            input("Resuelva el captcha y presione enter ")
            print("Continuando con el programa...")
        else:
            file.close()
            print("Cerrando el programa...")