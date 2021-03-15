import requests
from bs4 import BeautifulSoup

HOST = 'https://kino.kz/'
URL = 'https://kino.kz/movies_list?city=2'
HEARERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEARERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='poster')
    cards = []
    print(items)


html = get_html(URL)
get_content(html.text)