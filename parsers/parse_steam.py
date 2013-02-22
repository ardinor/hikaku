# -*- coding: utf-8 -*-
import time

from get_soup import get_soup
from config import STEAM_URLS


def parse_entry(entry):

    title = entry.find('h4').get_text()
    print repr(title)
    entry_url = entry.get('href')
    entry_url = entry_url[:entry_url.find('/?')]
    for i in entry.p.find_all('img'):
        if 'platform_linux' in i.get('src'):
            print 'Linux'
        elif 'platform_mac' in i.get('src'):
            print 'Mac'
        elif 'platform_win' in i.get('src'):
            print 'Win'
    t = entry.p.get_text().strip()
    categories = t[:t.find('-')].strip().split(', ')
    print categories
    released = entry.find(class_='col search_released').text
    print 'Released {}'.format(released)
    metascore = entry.find(class_='col search_metascore').text
    print 'Metascore {}'.format(metascore)
    t = entry.find(class_='col search_price')
    if t:
        full_price = None
        if t.findChild('span'):
            full_price = t.findChild('span').get_text()
        price = t.get_text()
        if full_price:
            price = price[price.find(full_price) + len(full_price):]
            full_price = float(full_price[1:])
            print 'Full price: %s' % full_price
        if price[1:].replace('.', '').isdigit():
            price = float(price[1:])
            print 'Price: %s' % price
        if full_price:
            discount = "%.2f" % (1 - price / full_price)
            print 'Discount of %s%%' % discount[2:]
    print '\n'


def full_check():

    pages = {}

    for i in [STEAM_URLS['GAMES_URL'], STEAM_URLS['DLC_URL']]:
        url = i.format('1')
        soup = get_soup(url)
        if soup:
            search_pag = soup.find(class_='search_pagination_right')
            search_a = search_pag.find_all('a')
            total_pages = int(search_a[len(search_a) - 2].text)
            pages[i] = total_pages
            print 'Steam - Total pages {}'.format(total_pages)
            time.sleep(3)

    #for i, j in pages.iteritems():
    #    for m in xrange(1, j + 1):
    #        url = i.format(str(m))
    #        soup = get_soup(url)
    #        if soup:
    #            for n in soup.find_all(class_='search_result_row'):
    #                parse_entry(n)
    #                time.sleep(randint(2, 7))


def specials_check():

    soup = get_soup(STEAM_URLS['SPECIALS_URL'])
    if soup:
        search_pag = soup.find(class_='search_pagination_right')
        search_a = search_pag.find_all('a')
        total_pages = int(search_a[len(search_a) - 2].text)
        print 'Steam - Total pages {}'.format(total_pages)
