from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
report = cg.get_coins_markets(vs_currency='usd')
print(report)

num = int(input("Enter: "))
counter = 0
while counter < num:
    counter += 1
    print(counter," - ", report[counter]['name'], report[counter]['market_cap'])


