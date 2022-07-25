import json
import requests
from datetime import datetime
import time

def get_glassnode_stats(date_start='01-01-2020', date_end='02-01-2020', display_currency='usd') -> dict:
    """Get on-chain cryptocurrency statistics from Glassnode for a specified date:
    Parameters:
    - date: date in format dd-mm-yyyy (gets converted to Unix timestamp)
    - display_currency: usd or native
    """
    API_KEY='INSERT_YOUR_API_KEY'
    start_datetime = datetime.strptime(date_start, '%d-%m-%Y')
    end_datetime = datetime.strptime(date_end, '%d-%m-%Y')
    start_unixtime = int(time.mktime(start_datetime.timetuple()))
    end_unixtime = int(time.mktime(end_datetime.timetuple()))

    result = dict(bitcoin={}, ethereum={}, litecoin={}, bitcoin_cash={})
    crypto_ids = ['BTC', 'ETH', 'LTC', 'BCH']

    crypto_names = {
        'BTC': 'bitcoin',
        'ETH': 'ethereum',
        'LTC': 'litecoin',
        'BCH': 'bitcoin_cash'
    }

    request_endpoints = {
        'tx_fees':'fees/volume_mean',
        'active_adresses':'addresses/active_count',
        'tx_count':'transactions/count',
        'tx_mean_size':'transactions/transfers_volume_mean',
        'non_zero_adress_count':'addresses/non_zero_count'
    }

    for coin in crypto_ids:
        payload = {'a':coin,'api_key': API_KEY, 's':start_unixtime, 'u':end_unixtime, 'i':'24h', 'c':'usd'}
        for metric in request_endpoints:
            if metric == 'non_zero_adress_count':
                payload['a'] = 'BTC'
                r = requests.get('https://api.glassnode.com/v1/metrics/'+request_endpoints[metric], payload)
                data = json.loads(r.content)
                data = data[0]
                result[crypto_names['BTC']][metric] = data['v']
            else:
                r = requests.get('https://api.glassnode.com/v1/metrics/'+request_endpoints[metric], payload)
                data = json.loads(r.content)
                data = data[0]
                result[crypto_names[coin]][metric] = data['v']

    return result
