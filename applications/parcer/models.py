

from django.db import models
from bs4 import BeautifulSoup
import requests

url = 'https://fitaudit.ru/food'

def get_html_page(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'lxml')
    return soup


def get_data(title):
    html = get_html_page(url)
    url2 = html.find('a', title=title)['href']
    html_page = get_html_page(url2)
    p = html_page.find('p', class_='him_bx__wrap')
    data = p.find_all('span', class_='js__msr_cc')

    calories = int(data[-6].text.split()[0])
    jiry = float(data[-5].text.split()[0].replace(',', '.'))
    belki = float(data[-4].text.split()[0].replace(',', '.'))
    uglevody = float(data[-3].text.split()[0].replace(',', '.'))
    voda = float(data[-2].text.split()[0].replace(',', '.'))
    zola = float(data[-1].text.split()[0].replace(',', '.'))

    output = {
        'calories': calories,
        'jiry': jiry,
        'belki': belki,
        'uglevody': uglevody,
        'voda': voda,
        'zola': zola
    }
    return 