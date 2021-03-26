import requests
from bs4 import BeautifulSoup
import re
from url_list_script import final_url_list

for url in final_url_list:

    try:
        r = requests.get(url)

        html = r.text

        soup = BeautifulSoup(html, 'lxml')

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

        with open("D:/python_arcticles/texts.txt", "a+") as myfile:
            try:
                myfile.write(lead_text)
            except:
                pass
            myfile.write(landing_text)
    except:
        continue
