import time
from stellar_sdk import Server


server = Server(horizon_url="https://horizon.stellar.org")
account_id = "GCSQRCJR77FHDITYON46VO5J47ZEOD5HXNM6FL3LJNTXAQ4D53G5DW6C"


key_last_modified_time = 'last_modified_time'
key_embedded = '_embedded'
key_records = 'records'


def selling_buying_offer(account_id):
    offers = server.offers().for_seller(account_id).call()
    offers_data = offers[key_embedded][key_records]

    # For control
    # print(json.dumps(offers_data, indent=4))

    for i in range(len(offers_data)):

        sentence =  ' '

        sentence += offers_data[i]['last_modified_time']
        sentence += ' '
        sentence += 'Kozak '
        sentence += "sells "
        sentence += offers_data[i]['amount']
        sentence += ' '
        sentence += offers_data[i]['selling']['asset_type']
        sentence += ' '

        sentence += 'for the price of '
        sentence +=offers_data[i]['price']
        sentence += ' '

        sentence +='of '
        sentence += offers_data[i]['buying']['asset_type']

        print(sentence)




while True:
    print('\n\n\n')
    selling_buying_offer(account_id)
    time.sleep(60)
