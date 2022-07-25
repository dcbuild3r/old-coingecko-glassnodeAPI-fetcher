import json
import requests

def get_coingeko_stats(date: str, display_currency: str) -> dict:
    """Get cryptocurrency statistics from CoinGecko for a specified date:
    
    Parameters:
    - date: date in format dd-mm-yyyy
    - display_currency: usd, eur, gbp, czk, btc, eth, ... 
    """
    crypto_ids = ['bitcoin', 'ethereum', 'litecoin', 'bitcoin-cash']
    crypto_names = {
        'bitcoin': 'bitcoin',
        'ethereum': 'ethereum',
        'litecoin': 'litecoin',
        'bitcoin-cash': 'bitcoin_cash'
    }
    payload={'date':date}
    result = dict()
    
    for coin in crypto_ids:
        r = requests.get('https://api.coingecko.com/api/v3/coins/'+coin+'/history/', params=payload)
        data = json.loads(r.content)
                    
        market_data = data['market_data']
        
        coin_result = {
            'symbol': data['symbol'],
            'market_cap': market_data['market_cap'][display_currency],
            'current_price': market_data['current_price'][display_currency],
            'total_volume': market_data['total_volume'][display_currency]
        }
        
        result[crypto_names[coin]] = coin_result 

    return result