# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import time
from random import randint

base_url = 'http://store.steampowered.com/search/?sort_by=&sort_order=ASC&page='

GAMES_URL = 'http://store.steampowered.com/search/?category1=998&page='
DLC_URL = 'http://store.steampowered.com/search/?category1=21&page='
SPECIALS_URL = 'http://store.steampowered.com/search/?specials=1&page='


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
    #if entry.p.find(class_='platform_img'):
    #    platform_img_src = entry.p.find(class_='platform_img').attrs['src']
    #    if 'platform_win' in platform_img_src:
    #        print 'Windows'
    #    elif 'platform_steamplay' in platform_img_src:
    #        print 'Steamplay'
    t = entry.p.get_text().strip()
    categories = t[:t.find('-')].strip().split(', ')
    print categories
    released = entry.find(class_='col search_released').text
    print 'Released {}'.format(released)
    # if t.find('Released') >= 0:
    #     released = t[t.find('Released') + 10:]
    #     print 'Released: %s' % released
    # elif t.find('Available') >= 0:
    #     released = t[t.find('Available') + 11:]
    #     print 'Available: %s' % released
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


def get_soup(url):

    f = urllib.urlopen(url)
    if f.getcode() != 404:
        html = f.read()
        return BeautifulSoup(html)
    else:
        return False


def full_check():

    pages = {}

    for i in [GAMES_URL, DLC_URL]:
        url = i + '1'
        soup = get_soup(url)
        if soup:
            search_pag = soup.find(class_='search_pagination_right')
            search_a = search_pag.find_all('a')
            total_pages = int(search_a[len(search_a) - 2].text)
            pages[i] = total_pages
            print 'Total pages {}'.format(total_pages)
            time.sleep(3)

    for i, j in pages.iteritems():
        for m in xrange(1, j + 1):
            url = i + str(m)
            soup = get_soup(url)
            if soup:
                for n in soup.find_all(class_='search_result_row'):
                    parse_entry(n)
                    time.sleep(randint(2, 7))


def specials_check():

    soup = get_soup(SPECIALS_URL)
    if soup:
        search_pag = soup.find(class_='search_pagination_right')
        search_a = search_pag.find_all('a')
        total_pages = int(search_a[len(search_a) - 2].text)
        print 'Total pages {}'.format(total_pages)

if __name__ == '__main__':

    full_check()
    specials_check()

        # for i in xrange(3):
        #     url = games_url + str(i + 1)
        #     print '\n\n%s' % url
        #     f = urllib.urlopen(url)
        #     html = f.read()
        #     soup = BeautifulSoup(html)
        #     for i in soup.find_all(class_='search_result_row'):
        #         parse_entry(i)

        #     time.sleep(3)