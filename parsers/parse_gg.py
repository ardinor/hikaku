# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2

ALL_URL = 'http://www.gamersgate.com/games?state=available&pg='

SPECIAL_OFFER_URL = 'http://www.gamersgate.com/games?filter=offers&state=available&pg='


def get_soup(url):

    req = urllib2.Request(url)
    req.add_header('User-agent', 'hikaku-bot[0.1]@github.com/ardinor')
    f = urllib2.urlopen(req)
    if f.getcode() != 404:
        html = f.read()
        return BeautifulSoup(html)
    else:
        return False


def parse_entry(entry):

    ttl = entry.find(class_='ttl')
    title = ttl.get('title')
    url = ttl.get('href')
    price = entry.find(class_='prtag').text

    print title, url, price


def full_check():

    url = ALL_URL + '1'
    soup = get_soup(url)
    if soup:
        inner = soup.find(class_='paginator').find(class_='inner')
        pgn_next = inner.find(class_='pgn_next')
        if pgn_next:
            total_pages = pgn_next.previous_sibling.text
            print total_pages

    for i in soup.find_all(class_='product_display'):
        parse_entry(i)

if __name__ == '__main__':

    full_check()
