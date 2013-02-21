# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import sys

from config import USER_AGENT

from reporting import reporting_info


def get_soup(url):

    """
    Give url, receive soup.
    """

    req = urllib2.Request(url)
    req.add_header('User-agent', USER_AGENT)
    f = urllib2.urlopen(req)
    if f.getcode() != 404:
        html = f.read()
        size = sys.getsizeof(html)
        reporting_info.total_size += size
        if 'store.steampowered.com' in url:
            reporting_info.steam_size += size
        elif 'gamersgate.com' in url:
            reporting_info.gamersgate_size += size
        elif 'greenmangaming.com' in url:
            reporting_info.greenman_size += size
        return BeautifulSoup(html)
    else:
        return False
