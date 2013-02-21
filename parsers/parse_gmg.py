# -*- coding: utf-8 -*-
import re
import time
from random import randint

from get_soup import get_soup

ALL_URL = 'http://www.greenmangaming.com/search/?q=&page='
BASE_URL = 'http://www.greenmangaming.com/'

HOT_DEALS_URL = 'http://www.greenmangaming.com/hot-deals/'
MIDWEEK_DEALS_URL = 'http://www.greenmangaming.com/midweek-deals/'
BARGAIN_BUCKET_URL = 'http://www.greenmangaming.com/bargain-bucket/'

#hot_deals = http://www.greenmangaming.com/games/browse/hot-deals/?page=3   ???


def parse_entry(entry):

    title = entry.h2.text.strip()
    print title
    url = BASE_URL + entry.a.get('href').strip()
    print url
    cover_url = entry.a.img.get('src').strip()
    print cover_url
    saving_percent = entry.find(class_='savings_percent')
    if saving_percent:
        saving_percent = re.sub('[^0-9]', '', saving_percent.text.strip())
        print saving_percent
    current_price = entry.find(class_='curPrice').text.strip()
    if current_price:
        current_price = current_price.replace('$', '')
        print current_price

    print '\n\n'


def parse_product_row(soup):

    for i in soup.find_all(class_='product-row'):
        ul = i.ul
        for j in ul.find_all('li', recuvsive=False):
            url = BASE_URL + j.a.get('href').strip()
            cover_url = j.a.img.get('src')
            title = j.a.get('title').strip()
            current_price = j.find(class_='curPrice').text.strip()
            current_price = current_price.replace('$', '')
            try:
                original_price = j.find(class_='lt').text.strip()
                original_price = original_price.replace('$', '')
                discount = "%.2f" % (1 - float(current_price) / float(original_price))
                discount = discount[2:]
            except AttributeError:
                pass
            print title, current_price, original_price, discount


def parse_hero_row(soup):

    for i in soup.find_all(class_='hero'):
        inner = i.find(class_='inner')
        url = BASE_URL + inner.a.get('href').strip()
        cover_url = inner.a.img.get('src')
        #title = inner.find(class_='title').text
        title = inner.a.img.get('alt')
        price = inner.find(class_='price')
        original_price = price.small
        if original_price:
            original_price = original_price.text.strip()
            original_price = re.sub('[^0-9\.]', '', original_price)
        current_price = price.text.strip()
        current_price = current_price[current_price.find('\n'):].strip()
        current_price = re.sub('[^0-9\.]', '', current_price)
        discount = "%.2f" % (1 - float(current_price) / float(original_price))
        discount = discount[2:]
        print title, current_price, original_price, discount


def full_check():

    url = ALL_URL + '1'
    soup = get_soup(url)
    if soup:
        total_pages = soup.find(title='Last page').text
        print 'GreenManGaming - Total pages {}'.format(total_pages)

    #for i in total_pages:
    #    for m in soup.find_all(class_='border-container clearfix'):
    #        parse_entry(m)
    #        time.sleep(randint(2, 7))


def specials_check():

    urls = [HOT_DEALS_URL, MIDWEEK_DEALS_URL, BARGAIN_BUCKET_URL]

    for i in urls:
        soup = get_soup(i)
        if i == HOT_DEALS_URL or i == BARGAIN_BUCKET_URL:
            parse_hero_row(soup)
            parse_product_row(soup)
        else:
            parse_product_row(soup)
        time.sleep(randint(2, 7))


if __name__ == '__main__':

    #full_check()
    specials_check()
