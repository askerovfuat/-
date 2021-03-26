import requests
from bs4 import BeautifulSoup
import re
from press_parser import all_urls
import csv
import pandas as pd

print(all_urls[:3])

data = []

for url in all_urls[:3]:

    try:
        r = requests.get(url)

        html = r.text

        soup = BeautifulSoup(html, 'lxml')

        date = soup.find(
            'div', class_='col-md-6 col-12 news-info-line_date').get_text()

        try:
            lead_text = soup.find('div', class_='lead-text').get_text()
        except:
            pass

        landing_text = soup.find('div', class_='landing-text').get_text()

        try:

            caption = soup.find('div', class_='caption').get_text()
            landing_text = landing_text.replace(caption, '')

        except:
            pass

    except:
        continue

    data.append([date, landing_text])


df = pd.DataFrame(data, columns=['date', 'landing_text'])

print(df)
