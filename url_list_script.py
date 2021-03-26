import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import time


try:

    browser = webdriver.Chrome()

    browser.get('https://cbr.ru/news/#_buttonLoadNextEvt')

    time.sleep(5)

    html = browser.page_source

    while True:

        browser.find_element_by_id("_buttonLoadNextEvt").click()

        time.sleep(1)


except:

    time.sleep(20)

    url_list = []

    url = 'https://cbr.ru/news/'
    base_url = 'https://cbr.ru'

    """ browser.get(url) """
    html = browser.page_source

    soup = BeautifulSoup(html, 'lxml')

    urls = soup.find('div', id='events_tab100').find_all('a',
                                                         class_='news_title')
    for url in urls:
        total_url = base_url + url.get('href')
        url_list.append(total_url)


final_url_list = url_list
