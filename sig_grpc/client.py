import grpc
# from io.lightcone.services.crypto_service import service_crypto_pb2, service_crypto_pb2_grpc
import lib.service_crypto_pb2 as service__crypto__pb2
import lib.service_crypto_pb2_grpc as service__crypto__pb2__grpc
import lib.data_order_pb2 as data__order__pb2
import lib.data_types_pb2 as data__types__pb2
import lib.data_types_pb2 as data__types__pb2

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
            exchange_id = 1,
            order_id = data__types__pb2.OrderID(value=70),
            account_id =data__types__pb2.AccountID(value=7),
            tokens = data__order__pb2.Tokens(
                token_s = data__types__pb2.TokenID(value = 0),
                token_b = data__types__pb2.TokenID(value = 2),
            ),
            amounts = data__order__pb2.TokenAmounts(
               amount_s = data__types__pb2.Amount(value = descToBytes(330000000000000000)), # bytes.fromhex(hex(100000000000000000000)[2:]) ), 
               amount_b = data__types__pb2.Amount(value = descToBytes(100000000000000000000)), # bytes.fromhex(hex(200000000000000000000)[2:]) ), 
            ),
            original = data__order__pb2.Original(
                max_fee_bips = data__types__pb2.Percentage(value = 20),
                all_or_none = False,
                buy = False,
                valid_since = 1569465280,
                valid_until = 1572057280,
                sign_info = data__order__pb2.Signs(
                    dual_auth_pub_key = data__types__pb2.EdDSAPubKey(
                        x = descToBytes(6674145034343560865324539436548640798922427529843778417647310928128880527219),
                        y = descToBytes(20475747943702752787633047864876878209331810697711316824740281085816304497780),
                    ),
                )
            ),
        ),
        priv_key = data__types__pb2.EdDSAPrivKey(value=descToBytes(1872535890))
    )
    response = client.signOrder(request)
    print("received:\n")
    print(response)
    print(int((response.signature.rx).hex(), 16))
    print(int((response.signature.ry).hex(), 16))
    print(int((response.signature.s).hex(), 16))
    return response

if __name__ == '__main__':
    run()
