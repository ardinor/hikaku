# -*- coding: utf-8 -*-
from get_soup import get_soup

ALL_URL = 'http://www.gamersgate.com/games?state=available&pg='

SPECIAL_OFFER_URL = 'http://www.gamersgate.com/games?filter=offers&state=available&pg='


def parse_entry(entry):

    ttl = entry.find(class_='ttl')
    title = ttl.get('title')
    url = ttl.get('href')
    price = entry.find(class_='prtag').text

    print title, price  # url,


def full_check():

    url = ALL_URL + '1'
    soup = get_soup(url)
    if soup:
        inner = soup.find(class_='paginator').find(class_='inner')
        pgn_next = inner.find(class_='pgn_next')
        if pgn_next:
            total_pages = pgn_next.previous_sibling.text
            print 'GamersGate - Total pages {}'.format(total_pages)

    #for i in xrange(1, total_pages + 1):
    #    url = ALL_URL + i
    #    soup = get_soup(url)
    #    for j in soup.find_all(class_='product_display'):
    #        parse_entry(i)

if __name__ == '__main__':

    full_check()
