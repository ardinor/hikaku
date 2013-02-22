# -*- coding: utf-8 -*-
from get_soup import get_soup
from config import GAMERSGATE_URLS

"""
GamersGate TODO:

- What to do about Bundles?
- Ignore Soundtracks?


DRM:See bundled products
Activation:Must be activated on Steam

DRM:Steamworks (Requires a third-party download and account)
Activation:Must be activated on Steam

DRM:DRM Free


Platform:PC/Mac
Platform:PC


Categories:Bonus Content, Soundtrack
DRM:See bundled products
"""


def parse_entry(entry):

    ttl = entry.find(class_='ttl')
    title = ttl.get('title')
    url = ttl.get('href')
    price = entry.find(class_='prtag').text

    print title, price  # url,


def parse_page(url):

    url = url + '1'
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


def full_check():

    parse_page(GAMERSGATE_URLS['ALL_URL'])


def special_check():

    parse_page(GAMERSGATE_URLS['SPECIAL_OFFER_URL'])
