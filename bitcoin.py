import apikey
import requests

headers = {
    'X-CMC_PRO_API_KEY': '3961abc5-31d6-40e9-8ebb-018bbff4745f',
    'Accepts': 'application/json'
}

params = {
    'start': '1',
    'limit': '5',
    'convert': 'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url,params = params,headers = headers).json()

coins = json['data']

print(coins)
for x in coins:
    print(x['symbol'],x['quote']['USD']['price'])