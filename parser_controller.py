# -*- coding: utf-8 -*-
import time
import datetime
import sys

from parsers import parse_steam, parse_gg, parse_gmg
from reporting import reporting_info


def full_check():

    start = time.time()
    parse_steam.full_check()
    taken = datetime.timedelta(seconds=time.time() - start).seconds
    reporting_info.total_time += taken
    reporting_info.steam_time += taken

    start = time.time()
    parse_gg.full_check()
    taken = datetime.timedelta(seconds=time.time() - start).seconds
    reporting_info.total_time += taken
    reporting_info.gamersgate_time += taken

    start = time.time()
    parse_gmg.full_check()
    taken = datetime.timedelta(seconds=time.time() - start).seconds
    reporting_info.total_time += taken
    reporting_info.greenman_time += taken

    print 'Time total {}'.format(reporting_info.total_time)
    print 'Steam time {}'.format(reporting_info.steam_time)
    print 'GamersGate time {}'.format(reporting_info.gamersgate_time)
    print 'GreenMan time {}'.format(reporting_info.greenman_time)

    print 'Total downloaded {}'.format(reporting_info.total_size)
    print 'Steam download {}'.format(reporting_info.steam_size)
    print 'GamersGate download {}'.format(reporting_info.gamersgate_size)
    print 'GreenMan download {}'.format(reporting_info.greenman_size)


def specials_check():

    #parse_steam.specials_check()
    parse_gg.full_check()
    #parse_gmg.specials_check()

if __name__ == '__main__':

    try:
        if sys.argv[1] == '-full':
            full_check()
        elif sys.argv[1] == '-specials':
            specials_check()
    except IndexError:
        specials_check()
