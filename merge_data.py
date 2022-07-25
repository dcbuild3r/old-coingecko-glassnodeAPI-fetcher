import requests
import json
from datetime import datetime, timedelta

from coingecko import get_coingeko_stats
from glassnode import get_glassnode_stats

def get_stats(date:str, display_currency='usd') -> dict:
    coingecko_ping = requests.get('https://api.coingecko.com/api/v3/ping')
    if coingecko_ping.ok:
        coingecko_data = get_coingeko_stats(date, 'usd')
    else:
        print('CoinGecko is down')
        return None

    datetime_begin = datetime.strptime(date, '%d-%m-%Y')
    datetime_end = datetime_begin + timedelta(days=1)

    date_begin = datetime_begin.strftime('%d-%m-%Y')
    date_end = datetime_end.strftime('%d-%m-%Y')

    glassnode_data = get_glassnode_stats(date_begin, date_end, 'usd')

    if glassnode_data == {}:
        print("Glassnode is down")
        return None

    crypto_names = ['bitcoin', 'ethereum', 'litecoin', 'bitcoin_cash']
    result = {
        'bitcoin':{},
        'ethereum':{},
        'litecoin':{},
        'bitcoin_cash':{}
    }
    for coin in crypto_names:
        coingecko_data_coin = coingecko_data[coin]
        glassnode_data_coin = glassnode_data[coin]
        result[coin] = {**coingecko_data_coin,**glassnode_data_coin}

    return result
