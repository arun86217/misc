#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from time import sleep

chrome_driver = "C:\\Users\\magggi\\Downloads\\chromedriver_win32\\chromedriver.exe"

chr = webdriver.Chrome(chrome_driver)

usr = ''
pas = ''

url = 'https://tm.udemy.com/'

chr.get(url)

chr.find_element_by_xpath('//*[@id="tm"]/div[1]/div[2]/div/div/div[2]/div[1]/div/a').click()

chr.find_element_by_xpath('//*[@id="userNameInput"]').send_keys(usr)

chr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys(pas)

chr.find_element_by_xpath('//*[@id="submitButton"]').click()

learn = 'https://tm.udemy.com/home/my-courses/learning/'

chr.get(learn)

details={}

from bs4 import BeautifulSoup

page = BeautifulSoup(chr.page_source , 'html.parser')

def recorder(page,pg):
    page = BeautifulSoup(chr.page_source , 'html.parser')
    print(f'scraping page {pg}')
    pg = pg + 1
    try:
        sleep(4)
        cards = page.find_all(attrs={"class":'card-wrapper'})[0]
        print(cards)
        card_s = cards.find_all(attrs={'role':'presentation'})
        for card in cards:
            details[card.div.img['alt']]= url[:-1] + card.a['href']
            print(f"{card.div.img['alt']} ====> {url[:-1] + card.a['href']}")
        courses = page.find(attrs={'class':'pagination pagination-expanded'})
        sleep(5)
        if courses.find(attrs={'class':'pagination-next udi udi-next'}):
            print('<------------------------------is it printning loop----------------------------->')
            chr.get(f"{learn}?p={pg}")
            sleep(5)
            recorder(page,pg)
        else:
            print('All Pages Scraping Done')
            exit()
    except:
        if pg>15:   # hardcode last page
            print(details)
            exit()
        else:
            pg = pg+1
            chr.get(f"{learn}?p={pg}")
            sleep(5)
            recorder(page,pg)

recorder(page,1)

''' improvements needed:

handling exceptions

adding wait with expected conditions

masking credentials

'''