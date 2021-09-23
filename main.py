from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
result = cg.get_coins_markets(vs_currency='usd')
print(result)

num = int(input("Enter number: "))
digit = 0
while digit < num:
    print(digit+1, " - ", result[digit]['name'], result[digit]['market_cap'])
    digit += 1


