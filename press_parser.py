import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import time

# Лишняя фигня, тыкает по порядку на цифры

""" n = 2

while n > 0:
    browser.find_element_by_link_text('{}'.format(n)).click()
    n = n + 1 """


base_url = 'https://old.cbr.ru/press/month_archive/?'
page_part = 'page='

all_urls = []


for i in range(2, 169):
    url_gen = base_url + page_part + str(i)
    r = requests.get(url_gen)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    press_urls = soup.find(
        'table', class_='text_and_dates').find_all('a')
    for element in press_urls:
        press_url = element.get('href')
        all_urls.append(press_url)
