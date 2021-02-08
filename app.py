#
import json
from stellar_sdk import Server, Account

server = Server(horizon_url="https://horizon.stellar.org")
account_id = "GD4FJH4UO2BVMXDYMJ6PODE7EVEDVP7SQR4ZSU227HPOIT4W4ITAP7UH"
last_cursor = 'now'  # or load where you left off - do I use it in the code???

# get a list of transactions submitted by a particular account
#transactions = server.transactions() \
#    .for_account(account_id) \
#    .call()
#print(transactions)

# get a list of offers submitted by a particular account
#offers = server.offers() \
#    .for_seller(account_id) \
#    .call()
#print(offers)
#print(json.dumps(offers, indent = 4))

################# another attempt - below is same as above but in one line only, but maybe lees readible
offers = server.offers().for_seller(account_id).call()
offers = offers['_embedded']['records']

#print JSON formatted list of active offers and all related data
print(json.dumps(offers, indent = 4))

print("\n*********\n")

#only print aset name and value of the offer
for i in range(len(offers)):
    if 'asset_code' in offers[i]['selling'].keys() :
        print( offers[i]['selling']['asset_code'] + ' offer amount is: ' + offers[i]['amount'] )
    else:
        print('XML' + ' offer amount is: ' + offers[i]['amount'] )
print("\n*********")
