# Interface for the CoinGecko and Glassnode APIs

### Crypto Stats
Statistics for selected crypto currencies - BTC, ETH, LTC, BCH

Command-line utility to print market data and onchain data to the console.

#### APIs used:
- https://www.coingecko.com/en/api#explore-api - market data
- https://docs.glassnode.com - onchain data

### Dependencies:
Dependencies are located in `requirements.txt`<br> 
To install them run: `pip install -r requirements.txt`

### Usage:

Insert your Glassnode API KEY in `glassnode.py`.

Make `run.py` executable by running:
`chmod +x run.py` <br>
And then run: `./run.py [date(%d-%m-%Y)] [display_currency(usd,native)]`

#### Market data:
- market cap
- price (close time for UTC)
- change (24h)
- 24h volume

#### Onchain data:
- average fee for tx
- num of active addresses
- average num of txs/24h
- average size of single tx/24h
- num of addresses with non-zero balance

```
 ./run.py 30-12-2017 usd

>>> {
   "bitcoin": {
      "symbol": "btc",
      "market_cap": 228445816988.881,
      "current_price": 13620.3618741461,
      "total_volume": 3600481281.03768,
      "tx_fees": 32.32153712955091,
      "active_adresses": 1094021,
      "tx_count": 353824,
      "tx_mean_size": 95014.72717287869,
      "non_zero_adress_count": 26517339
   },
   "ethereum": {
      "symbol": "eth",
      "market_cap": 71238101432.8975,
      "current_price": 736.909191519636,
      "total_volume": 1306193221.81905,
      "tx_fees": 0.6787125022437158,
      "active_adresses": 543083,
      "tx_count": 1090191,
      "tx_mean_size": 13321.89684725972
   },
   "litecoin": {
      "symbol": "ltc",
      "market_cap": 12185489808.1574,
      "current_price": 223.400325158751,
      "total_volume": 569490495.299767,
      "tx_fees": 0.369016226768022,
      "active_adresses": 394056,
      "tx_count": 156079,
      "tx_mean_size": 55919.77483335565
   },
   "bitcoin_cash": {
      "symbol": "bch",
      "market_cap": 39862630089.0388,
      "current_price": 2360.84140670088,
      "total_volume": 772369324.027622,
      "tx_fees": 0.2997519928829722,
      "active_adresses": 319068,
      "tx_count": 43305,
      "tx_mean_size": 70276.83441223162
   }
}
```

#### extra info:
- requests are handled using the requests pip package
