# -*- coding: utf-8 -*-

USER_AGENT = 'hikaku-bot[0.1]@github.com/ardinor'

STEAM_URLS = {
    'GAMES_URL': 'http://store.steampowered.com/search/?category1=998&page={}',
    'DLC_URL': 'http://store.steampowered.com/search/?category1=21&page={}',
    'SPECIALS_URL': 'http://store.steampowered.com/search/?specials=1&page={}'
    }

GAMERSGATE_URLS = {
    'ALL_URL': 'http://www.gamersgate.com/games?state=available&pg=',
    'SPECIAL_OFFER_URL': 'http://www.gamersgate.com/games?filter=offers&state=available&pg='
    }

GREENMAN_URLS = {
    'ALL_URL': 'http://www.greenmangaming.com/search/?q=&page=',
    'BASE_URL': 'http://www.greenmangaming.com/',
    'HOT_DEALS_URL': 'http://www.greenmangaming.com/hot-deals/',
    'MIDWEEK_DEALS_URL': 'http://www.greenmangaming.com/midweek-deals/',
    'BARGAIN_BUCKET_URL': 'http://www.greenmangaming.com/bargain-bucket/'
    }

ORIGIN_URLS = {
    'ALL_URL': 'http://store.origin.com/store/ea/en_US/DisplayCategoryProductListPage/ThemeID.718200/categoryID.8831900/childCategoryID.8831900',
    'PAGE_URL': 'http://store.origin.com/store/?Action=DisplayCategoryProductListPage&SiteID=ea&Locale=en_US&CallingPageID=CategoryProductListPage&ORIG_VALUE_categoryID=8831900&categoryID=8831900&ORIG_VALUE_childCategoryID=8831900&childCategoryID=8831900&itemIdx={}'
}
