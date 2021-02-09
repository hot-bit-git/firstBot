import requests
import json

# Get market data from Stellar ticker
r = requests.get('https://ticker.stellar.org/markets.json')

json_obj = r.json()

# For control
# print(json.dumps(json_obj, indent=4, sort_keys=True))

pairs = json_obj['pairs']
# print(json.dumps(pairs, indent=4, sort_keys=True))
# print(pairs)

name_of_pair = 'XLM_XRP'

for pair in pairs:
    if pair['name'] == name_of_pair:
        price_XLM_XRP = pair['price']
        price_XRP_XLM = 1/price_XLM_XRP

        print('XLM / XRP = ' + "{:.18f}".format(price_XLM_XRP))
        print('XRP / XLM = ' + "{:.18f}".format(price_XRP_XLM))






