import grpc
# from io.lightcone.services.crypto_service import service_crypto_pb2, service_crypto_pb2_grpc
import service_crypto_pb2 as service__crypto__pb2
import service_crypto_pb2_grpc as service__crypto__pb2__grpc
import data_order_pb2 as data__order__pb2
import data_types_pb2 as data__types__pb2
import data_types_pb2 as data__types__pb2

_HOST = '192.168.1.167'
_PORT = '50052'
def hexToBytes(hex):
    hex = hex[2:]
    if len(hex) % 2 != 0:
        hex = '0' + hex
    return bytes.fromhex(hex)

def descToBytes(desc):
    hexStr = hex(desc)
    hexStr = hexStr[2:]
    if len(hexStr) % 2 != 0:
        hexStr = '0' + hexStr
    return bytes.fromhex(hexStr)

def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = service__crypto__pb2__grpc.CryptoServiceStub(channel=conn)
    print(len(hex(100000000000000000000)))
    request = service__crypto__pb2.SignOrderRequest (
        order = data__order__pb2.Order(
            exchange_id = 2,
            order_id = data__types__pb2.OrderID(value=0),
            account_id =data__types__pb2.AccountID(value=14),
            tokens = data__order__pb2.Tokens(
                token_s = data__types__pb2.TokenID(value = 1),
                token_b = data__types__pb2.TokenID(value = 3),
            ),
            amounts = data__order__pb2.TokenAmounts(
               amount_s = data__types__pb2.Amount(value = descToBytes(100000000000000000000)), # bytes.fromhex(hex(100000000000000000000)[2:]) ), 
               amount_b = data__types__pb2.Amount(value = descToBytes(200000000000000000000)), # bytes.fromhex(hex(200000000000000000000)[2:]) ), 
            ),
            original = data__order__pb2.Original(
                max_fee_bips = data__types__pb2.Percentage(value = 20),
                all_or_none = False,
                buy = True,
                valid_since = 1562889050,
                valid_until = 1562924050,
                sign_info = data__order__pb2.Signs(
                    dual_auth_pub_key = data__types__pb2.EdDSAPubKey(
                        x = bytes.fromhex(hex(8809204123973366120824088099131781443029836489874324209184159313707575442374)[2:]),
                        y = bytes.fromhex(hex(13988417089423714365999155658785932995359651021112875121671679566610495100815)[2:]),
                    ),
                )
            ),
        ),
        priv_key = data__types__pb2.EdDSAPrivKey(value=bytes.fromhex(hex(86710760873727)[2:]))
    )
    response = client.signOrder(request)
    print("received:\n")
    print(response)

if __name__ == '__main__':
    run()
