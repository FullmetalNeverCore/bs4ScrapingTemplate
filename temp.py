import requests 
import asyncio 
from bs4 import BeautifulSoup as bs

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0', 'accept': '*/*'}
global url 
url = "http://google.com"

def get_html(url, params=None):
    r = requests.get(url,headers=HEADERS, params=params)
    return r 

def get_content():
    html = get_html(url)
    if html.status_code == 200:
        print("200")
        get_text(html.text)
    else:
        print("Err" + html.status_code)

def get_text(html):
    soup = bs(html, 'html.parser')
    itms = soup.findAll('div', class_='o3j99 c93Gbe')
    prc = []
    for itm in itms:
        prc.append(
            itm.find('div',class_='uU7dJb').text
        )
    print(str(prc))

get_content()