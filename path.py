#
#this script creates a path payment on the mainnet
# aYOUR-SECRET-KEYa change for a secret key for account sending the payment 
#
from stellar_sdk import Keypair, Server, TransactionBuilder, Network, Asset
#from time import sleep
#sleep(1.05)

server = Server(horizon_url="https://horizon.stellar.org")
source_keypair = Keypair.from_secret("aYOUR-SECRET-KEYa")

source_account = server.load_account(account_id=source_keypair.public_key)

# path - tokens to go through on the path to send CENTUS and receive XLM
path = [
    Asset("USD", "GDUKMGUGDZQK6YHYA5Z6AY2G4XDSZPSZ3SW5UN3ARVMO6QSRDWP5YLEX"),
    Asset("USDC", "GA5ZSEJYB37JRC5AVCIA5MOP4RHTM335X2KGX3IHOJAPP5RE34K4KZVN"),
#    Asset("XLM", None)
#    Asset("DBC", "GBHD5TDFXKKZB32TEE7T6OM4WWME4X27DTVSVO26ZVZYWMWN2MT2552X"),
#    Asset("CENTUS", "GAKMVPHBET4T7DPN32ODVSI4AA3YEZX2GHGNNSBGFNRQ6QEVKFO4MNDZ"),
#    Asset("USD", "GB2O5PBQJDAFCNM2U2DIMVAEI7ISOYL4UJDTLN42JYYXAENKBWY6OBKZ"),
]


#account "aYOUR-SECRET-KEYa" will try to send max 5.0 CENTUS to GBEC....FUXX, and GBEC....FUXX should receive exactly 2.0 XLM. 
transactionX = TransactionBuilder(
    source_account=source_account, network_passphrase=Network.PUBLIC_NETWORK_PASSPHRASE, base_fee=100) \
    .append_path_payment_strict_receive_op(destination="GBECOMOO5N6NV7QUOHPD6OT2KR6KLAON6R4V223SR4XNN2YXA5NKFUXX",
                            send_code="CENTUS", send_issuer="GAKMVPHBET4T7DPN32ODVSI4AA3YEZX2GHGNNSBGFNRQ6QEVKFO4MNDZ", send_max="5.0", dest_code="XLM",
                            dest_issuer=None,
                            dest_amount="2.0", path=path) \
    .set_timeout(30) \
#valid for max 30s
    .build()
transactionX.sign(source_keypair)
response = server.submit_transaction(transactionX)
