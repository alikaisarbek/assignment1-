At first we need here pull data from source : coingeko.com

taked api from CoinGeckoApi from pycoingecko 
pulled with CoinGeckoApi 
in list cg.get_coins_markets you can get coince price, market cup and ather data
list created like array

result = cg.get_coins_markets(vs_currency='usd')
after that we can get data using this part code

result[counter]['name'], result[counter]['market_cap']
