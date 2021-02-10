import json
import time
from quotes import values_of_pair
from stellar_sdk import Server


server = Server(horizon_url="https://horizon.stellar.org")
account_id = "GCSQRCJR77FHDITYON46VO5J47ZEOD5HXNM6FL3LJNTXAQ4D53G5DW6C"
account_name = 'Kozak'

# account_id = "GA5OGZYOBTXBWTE5A6LXUCCWMUP7LYIS252DGEKBQ4IMFMKPTVMEK7LA"
# account_name = 'JakieśKonto'

key_last_modified_time = 'last_modified_time'
key_embedded = '_embedded'
key_records = 'records'
key_amount = 'amount'
key_buying = 'buying'
key_selling = 'selling'
key_price = 'price'


def name_of_cryptocurrency(in_offers_data):
    if in_offers_data['asset_type'] == 'native':
        return 'XLM'
    else:
        return in_offers_data['asset_code']


def is_buying_XML(in_offers_data):
    if in_offers_data['buying']['asset_type'] == 'native':
        return True
    else:
        return False



def selling_buying_offer(account_id):
    offers = server.offers().for_seller(account_id).call()
    offers_data = offers[key_embedded][key_records]

    # For control
    # print(json.dumps(offers, indent=4))

    for i in range(len(offers_data)):

        sentence =  ''

        sentence += offers_data[i]['last_modified_time']
        sentence += ' '
        sentence += account_name

        # Decision if buying XLM or selling XLM. Buying means that will be more XLM. Selling means it will be less XLM
        if(is_buying_XML(offers_data[i])):

            sentence += " BUYING "

            amount_of_XLS = float(offers_data[i][key_amount])*float(offers_data[i][key_price])
            sentence += "{:.8f}".format(amount_of_XLS)

            sentence += ' '

            sentence += name_of_cryptocurrency(offers_data[i][key_buying])
            sentence += ' '

            price_of_XRP_XLS = 1/float(offers_data[i][key_price])

            sentence += ' for '
            sentence += name_of_cryptocurrency(offers_data[i][key_selling])

            sentence += ' at the price of '+"{:.8f}".format(price_of_XRP_XLS)

            sentence += name_of_cryptocurrency(offers_data[i][key_buying])
            sentence += '/'
            sentence += name_of_cryptocurrency(offers_data[i][key_selling])

        else:

            sentence += " SELLING "
            sentence += offers_data[i]['amount']
            sentence += ' '
            sentence += name_of_cryptocurrency(offers_data[i]['selling'])
            sentence += ' '

            sentence += ' for '
            sentence += name_of_cryptocurrency(offers_data[i][key_buying])

            sentence += ' at the price of '
            sentence += offers_data[i]['price']
            sentence += ' '

            sentence += name_of_cryptocurrency(offers_data[i][key_selling])
            sentence += '/'
            sentence += name_of_cryptocurrency(offers_data[i][key_buying])

        print(sentence)




while True:

    print('Start')
    selling_buying_offer(account_id)
    print('\n')
    values_of_pair()
    time.sleep(60)

