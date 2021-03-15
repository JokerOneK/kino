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

    for item in items:
        cards.append(
            {
                'href': str(item.get('href'))
            }
        )
    return cards


def get_schedule(html):
    soup = BeautifulSoup(html, 'html.parser')
    times = soup.find_all('div', class_='schedule-time')
    cinemas = soup.find_all('div', class_='cinema-title')
    schedules = dict(zip(cinemas.text, times.text))
    print(schedules.text)







html = get_html(URL)
movies = get_content(html.text)

movie_url = 'https://kino.kz/'
for movie in movies:

    movie_html = get_html(movie_url + "".join(movie.values()))
    # print(movie_url + "".join(movie.values()))
    # print(movie_html.text)
    get_schedule(movie_html)



