import bs4
from requests import get
from bs4 import BeautifulSoup
from re import search

def get_urls(search_string):
    temp = []
    url = 'http://www.google.com/search'
    payload = {'q': search_string}
    my_headers = {'User-agent': 'Mozilla/11.0'}
    r = get(url, params=payload, headers=my_headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    divtags = soup.find_all('div', class_='kCrYT')

    for div in divtags:
        try:
            temp.append(search('url\?q=(.+?)\&sa', div.a['href']).group(1))
        except:
            continue
    return temp