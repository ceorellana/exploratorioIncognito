import requests
import contextlib
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
import time
import lxml.html as LH
import lxml.html.clean as clean

# class paperItem(Item):
#     # define the fields for your item here like:
#     title = Field()
#     price = Field()
#     #url = scrapy.Field()
#     description = Field()
#     address = Field()

# driver = webdriver.Chrome("C:\\Users\\Carlo Orellana\\Downloads\\chromedriver.exe")
# driver.get('https://scholar.google.com/scholar?hl=es&as_sdt=0%2C5&q=programming+language&btnG=&oq=programming+')
# time.sleep(1)

# r = requests.get("https://scholar.google.com/scholar?q=programming+language&hl=es&num=20&as_sdt=0&as_vis=1")
# soup  = BeautifulSoup(r.content)
# text = soup.get_text()
# print (text)

# elem = driver.page_source
# time.sleep(0.2)
# post_elems = driver.page_source
# soup = BeautifulSoup(post_elems)
# print(soup.prettify())

def getWords(url,browser):
    ignore_tags = ('script', 'noscript', 'style')
    browser.get(url)  # Load page
    content = browser.page_source
    cleaner = clean.Cleaner()
    content = cleaner.clean_html(content)
    with open('source.html', 'w') as f:
        f.write(content.encode('utf-8'))
    doc = LH.fromstring(content)
    with open('result.txt', 'w') as f:
        for elt in doc.iterdescendants():
            if elt.tag in ignore_tags: continue
            text = elt.text or ''
            tail = elt.tail or ''
            words = ' '.join((text, tail)).strip()
            if words:
                words = words.encode('utf-8')
                f.write(words + '\n')

url="https://scholar.google.com/scholar?hl=es&as_sdt=0%2C5&q=programming+language&btnG=&oq=programming+"
browser = webdriver.Chrome("C:\\Users\\Carlo Orellana\\Downloads\\chromedriver.exe")
browser.get(url)  # Load page
raw_input("Resuelva los captchas (si los hubiese), deseleccione citas y patentes y presione enter para comenzar ")


isPresent = len(browser.find_elements_by_xpath('//*[@id="gs_n"]/center/table/tbody/tr/td[12]/a')) >0
i = 1
while (isPresent):
    paperUrl = browser.find_elements_by_class_name('gs_rt')
    print("Pagina " + str(i))
    for paper in paperUrl:
        link = paper.find_element_by_tag_name('a')
        print(link.get_attribute('href'))
    user = browser.find_element_by_xpath('//*[@id="gs_n"]/center/table/tbody/tr/td[12]/a')
    user.click()
    time.sleep(2)
    isPresent = len(browser.find_elements_by_xpath('//*[@id="gs_n"]/center/table/tbody/tr/td[12]/a')) > 0
    i+=1
    if (isPresent == False):
        print("1. Captcha\n2. Fin de busqueda")
        op = int(raw_input("Seleccione lo ocurrido: "))
        if (op == 1):
            isPresent == True
            raw_input("Resuelva el captcha y presione enter ")
            print("Continuando con el programa...")
        else:
            print("Cerrando el programa...")