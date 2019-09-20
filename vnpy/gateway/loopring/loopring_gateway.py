"""
Gateway for Loopring Crypto Exchange.
"""

import urllib
import hashlib
import hmac
import time
import json
from copy import copy
from datetime import datetime, timedelta
from enum import Enum
from threading import Lock

from vnpy.api.rest import RestClient, Request
from vnpy.api.websocket import WebsocketClient
from vnpy.trader.constant import (
    Direction,
    Exchange,
    Product,
    Status,
    OrderType,
    Interval
)
from vnpy.trader.gateway import BaseGateway
from vnpy.trader.object import (
    TickData,
    OrderData,
    TradeData,
    AccountData,
    ContractData,
    BarData,
    OrderRequest,
    CancelRequest,
    SubscribeRequest,
    HistoryRequest
)
from vnpy.trader.event import EVENT_TIMER
from vnpy.event import Event

from ethsnarks.eddsa import PureEdDSA
from ethsnarks.field import FQ


REST_HOST = "http://13.231.113.1:31610"
WEBSOCKET_TRADE_HOST = "ws://13.231.113.1:31610/v1/ws"
WEBSOCKET_DATA_HOST = "ws://13.231.113.1:31610/v1/ws"

STATUS_LOOPRING2VT = {
    "NEW": Status.NOTTRADED,
    "PARTIALLY_FILLED": Status.PARTTRADED,
    "FILLED": Status.ALLTRADED,
    "CANCELED": Status.CANCELLED,
    "REJECTED": Status.REJECTED
}

ORDERTYPE_VT2LOOPRING = {
    OrderType.LIMIT: "LIMIT",
    OrderType.MARKET: "MARKET"
}
ORDERTYPE_LOOPRING2VT = {v: k for k, v in ORDERTYPE_VT2LOOPRING.items()}

DIRECTION_VT2LOOPRING = {
    Direction.LONG: "BUY",
    Direction.SHORT: "SELL"
}
DIRECTION_LOOPRING2VT = {v: k for k, v in DIRECTION_VT2LOOPRING.items()}

INTERVAL_VT2LOOPRING = {
    Interval.MINUTE: "1m",
    Interval.HOUR: "1h",
    Interval.DAILY: "1d",
}

TIMEDELTA_MAP = {
    Interval.MINUTE: timedelta(minutes=1),
    Interval.HOUR: timedelta(hours=1),
    Interval.DAILY: timedelta(days=1),
}


class Security(Enum):
    NONE = 0
    SIGNED = 1
    API_KEY = 2


symbol_name_map = {}


class LoopringGateway(BaseGateway):
    """
    VN Trader Gateway for Loopring connection.
    """

    default_setting = {
        "key": "",
        "secret": "",
        "session_number": 3,
        "proxy_host": "",
        "proxy_port": 0,
    }

    exchanges = [Exchange.LOOPRING]

    def __init__(self, event_engine):
        """Constructor"""
        super().__init__(event_engine, "LOOPRING")

        self.trade_ws_api = LoopringTradeWebsocketApi(self)
        self.market_ws_api = LoopringDataWebsocketApi(self)
        self.rest_api = LoopringRestApi(self)

        self.event_engine.register(EVENT_TIMER, self.process_timer_event)

    def connect(self, setting: dict):
        """"""
        key = setting["key"]
        secret = setting["secret"]
        session_number = setting["session_number"]
        proxy_host = setting["proxy_host"]
        proxy_port = setting["proxy_port"]
        address = setting["address"]

        self.rest_api.connect(key, secret, session_number,
                              proxy_host, proxy_port, address)
        self.market_ws_api.connect(proxy_host, proxy_port)

    def subscribe(self, req: SubscribeRequest):
        """"""
        self.market_ws_api.subscribe(req)

    def send_order(self, req: OrderRequest):
        """"""
        return self.rest_api.send_order(req)

    def cancel_order(self, req: CancelRequest):
        """"""
        self.rest_api.cancel_order(req)

    def query_account(self):
        """"""
        pass

    def query_position(self):
        """"""
        pass

    def query_history(self, req: HistoryRequest):
        """"""
        return self.rest_api.query_history(req)

    def close(self):
        """"""
        self.rest_api.stop()
        self.trade_ws_api.stop()
        self.market_ws_api.stop()

    def process_timer_event(self, event: Event):
        """"""
        self.rest_api.keep_user_stream()


class LoopringRestApi(RestClient):
    """
    LOOPRING REST API
    """

    def __init__(self, gateway: LoopringGateway):
        """"""
        super().__init__()

        self.gateway = gateway
        self.gateway_name = gateway.gateway_name

        self.trade_ws_api = self.gateway.trade_ws_api

        self.key = ""
        self.secret = ""

        self.user_stream_key = ""
        self.keep_alive_count = 0
        self.recv_window = 5000
        self.time_offset = 0

        self.order_count = 1_000_000
        self.order_count_lock = Lock()
        self.connect_time = 0

        self.address = ""
        self.publicKeyX = ""
        self.publicKeyY = ""
        self.lrcTokenId = 2
        self.ethTokenId = ""
        self.accountId = 0

        self.orderHash = []
        self.orderId = [None] * 256

    def sign(self, request):
        """
        Generate LOOPRING signature.
        """
        return request
        self.gateway.write_log("call sign")
        self.gateway.write_log(request)
        security = request.data["security"]
        if security == Security.NONE:
            request.data = None
            return request

        if request.params:
            path = request.path + "?" + urllib.parse.urlencode(request.params)
        else:
            request.params = dict()
            path = request.path

        if security == Security.SIGNED:
            timestamp = int(time.time() * 1000)

            if self.time_offset > 0:
                timestamp -= abs(self.time_offset)
            elif self.time_offset < 0:
                timestamp += abs(self.time_offset)

            request.params["timestamp"] = timestamp

            query = urllib.parse.urlencode(sorted(request.params.items()))
            signature = hmac.new(self.secret, query.encode(
                "utf-8"), hashlib.sha256).hexdigest()

            query += "&signature={}".format(signature)
            path = request.path + "?" + query

        request.path = path
        request.params = {}
        request.data = {}

        # Add headers
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "X-MBX-APIKEY": self.key
        }

        if security in [Security.SIGNED, Security.API_KEY]:
            request.headers = headers

        return request

    def connect(
        self,
        key: str,
        secret: str,
        session_number: int,
        proxy_host: str,
        proxy_port: int,
        address: str
    ):
        """
        Initialize connection to REST server.
        """
        self.key = key
        self.secret = secret.encode()
        self.proxy_port = proxy_port
        self.proxy_host = proxy_host
        self.address = address

        self.connect_time = (
            int(datetime.now().strftime("%y%m%d%H%M%S")) * self.order_count
        )

        self.init(REST_HOST, proxy_host, proxy_port)
        self.start(session_number)

        self.gateway.write_log("REST API启动成功")

        self.gateway.write_log("start query_time")
        self.query_time()
        self.gateway.write_log("start query_account")
        self.query_account()
        #self.query_order()
        self.gateway.write_log("start query_contract")
        self.query_contract()
        #self.start_user_stream()
        #self.gateway.write_log("trade_ws_api connect")
        #self.trade_ws_api.connect(WEBSOCKET_DATA_HOST, self.proxy_host, self.proxy_port)

    def query_time(self):
        """"""
        data = {
            "security": Security.NONE
        }
        path = "/api/v1/timestamp"

        added_request = self.add_request(
            "GET",
            path,
            callback=self.on_query_time,
            data=data
        )
        self.gateway.write_log(added_request)
        return added_request

    def query_account(self):
        """"""
        data = {"security": Security.NONE}

        param = {
            "address": self.address
        }

        self.add_request(
            method="GET",
            path="/api/v1/account",
            callback=self.on_query_account,
            params=param,
            data=data
        )

    def query_balance(self):
        """"""
        data = {"security": Security.NONE}

        param = {
            "accountId": self.accountId
        }

        self.add_request(
            method="GET",
            path="/api/v1/user/balances",
            callback=self.on_query_balance,
            params=param,
            data=data
        )

    def query_order(self):
        """"""
        data = {"security": Security.NONE}

        self.add_request(
            method="GET",
            path="/api/v1/order",
            callback=self.on_query_order,
            data=data
        )

    def query_orders(self):
        """"""
        data = {"security": Security.NONE}

        params = {
            "accountId": self.accountId
        }

        self.add_request(
            method="GET",
            path="/api/v1/orders",
            callback=self.on_query_orders,
            params=params,
            data=data
        )

    def query_contract(self):
        """"""
        data = {
            "security": Security.NONE
        }
        params = {
            "symbols": "LRC"
        }
        self.add_request(
            method="GET",
            path="/api/v1/tokenInfo",
            callback=self.on_query_contract,
            params=params,
            data=data
        )

    def _new_order_id(self):
        """"""
        with self.order_count_lock:
            self.order_count += 1
            return self.order_count

    def send_order(self, req: OrderRequest):
        """"""
        self.gateway.write_log("send_order")
        orderid = str(self.connect_time + self._new_order_id())
        order = req.create_order_data(
            orderid,
            self.gateway_name
        )
        self.gateway.on_order(order)

        exchangeId = 1
        orderId = self.orderId[0]

        validSince = int(time.time()*1000)
        validUntil = validSince + 24 * 60 * 60 * 1000
        maxFeeBips = 20
        allOrNone = 1
        buy = 1

        msg_parts = [
            FQ(int(exchangeId), 1 << 32), FQ(int(orderId), 1 << 20),
            FQ(int(self.accountId), 1 << 20),
            FQ(int(self.publicKeyY), 1 << 254), FQ(int(self.publicKeyY), 1 << 254),
            FQ(int(self.lrcTokenId), 1 << 8), FQ(int(self.lrcTokenId), 1 << 8),
            FQ(int(req.volume), 1 << 96), FQ(int(req.volume), 1 << 96),
            FQ(int(allOrNone), 1 << 1), FQ(int(validSince), 1 << 32), FQ(int(validUntil), 1 << 32),
            FQ(int(maxFeeBips), 1 << 6),
            FQ(int(buy), 1 << 1)
        ]
        message = PureEdDSA.to_bits(*msg_parts)

        self.gateway.write_log(int(self.secret))
        signedMessage = PureEdDSA.sign(message, FQ(int(self.secret)))

        hash = PureEdDSA().hash_public(signedMessage.sig.R, signedMessage.A, signedMessage.msg)

        msg = {
            "exchangeId": exchangeId,
            "orderId": orderId,
            "accountId": self.accountId,
            "tokenSId": 0,
            "tokenBId": self.lrcTokenId,
            "amountS": "100000000000000000",
            "amountB": "100000000000000000000",
            "hash": str(hash),
            "maxFeeBips": maxFeeBips,
            "validSince": validSince,
            "validUntil": validUntil,
            "dualAuthPubKeyX": str(self.publicKeyX),
            "dualAuthPubKeyY": str(self.publicKeyY),
            "dualAuthPrivKey": str(self.publicKeyY),
            "tradingPubKeyX": str(self.publicKeyX),
            "tradingPubKeyY": str(self.publicKeyY),
            "tradingSigRx": str(signedMessage.sig.R.x),
            "tradingSigRy": str(signedMessage.sig.R.y),
            "tradingSigS": str(signedMessage.sig.s),
            "clientOrderId": ""
        }

        '''
        msg = {
            "exchangeId": 1,
            "orderId": 0,
            "accountId": 100,
            "tokenSId": 2,
            "tokenBId": 0,
            "amountS": "150000000000000000000",
            "amountB": "10000000000000000",
            "hash": "14504358714580556901944011952143357684927684879578923674101657902115012783290",
            "maxFeeBips": 20,
            "validSince": 1567052201,
            "validUntil": 1569645201,
            "dualAuthPubKeyX": "3361199864829102879089761359041084639986510274234372880847316559184665065303",
            "dualAuthPubKeyY": "9171799468103969055304541734277260692003757276767513327577616030089521138017",
            "dualAuthPrivKey": "47371961212603178341706",
            "tradingPubKeyX": "16309728762011835354894444201372057648592320986680190035881441620421033294098",
            "tradingPubKeyY": "20132776233802896271927059541627812930965780555542811823387317755220841280391",
            "tradingSigRx": "15179969700843231746888635151106024191752286977677731880613780154804077177446",
            "tradingSigRy": "8103765835373541952843207933665617916816772340145691265012430975846006955894",
            "tradingSigS": "4462707474665244243174020779004308974607763640730341744048308145656189589982",
            "clientOrderId": ""
        }
        '''


        self.gateway.write_log(msg)

        headers = {
            "Content-Type": "application/json"
        }

        self.add_request(
            method="POST",
            path="/api/v1/order",
            callback=self.on_send_order,
            data=json.dumps(msg),
            #params=params,
            headers=headers,
            #extra=order,
            on_error=self.on_send_order_error,
            on_failed=self.on_send_order_failed
        )

        return order.vt_orderid

    def cancel_order(self, req: CancelRequest):
        """"""
        if len(self.orderHash) < 1:
            self.gateway.write_log("There's no order to cancel")
            return

        data = {
            "security": Security.NONE
        }

        params = {
            "accountId": self.accountId,
            "orderHash": self.orderHash[int(req.orderid)]
        }

        self.add_request(
            method="DELETE",
            path="/api/v1/orders",
            callback=self.on_cancel_order,
            params=params,
            data=data
        )

    def start_user_stream(self):
        self.gateway.write_log("start_user_stream")
        """"""
        data = {
            "security": Security.NONE
        }

        self.add_request(
            method="POST",
            path="/api/v1/stream",
            callback=self.on_start_user_stream,
            data=data
        )

    def keep_user_stream(self):
        """"""
        self.keep_alive_count += 1
        if self.keep_alive_count < 1800:
            return

        data = {
            "security": Security.API_KEY
        }

        params = {
            "listenKey": self.user_stream_key
        }

        self.add_request(
            method="PUT",
            path="/api/v1/userDataStream",
            callback=self.on_keep_user_stream,
            params=params,
            data=data
        )

    def on_query_time(self, data, request):
        """"""
        self.gateway.write_log("on_query_time:")
        self.gateway.write_log(data)
        local_time = int(time.time() * 1000)
        server_time = int(data["timestamp"])
        self.time_offset = local_time - server_time

    def on_query_account(self, data, request):
        """"""
        self.gateway.write_log("on_query_account")
        self.gateway.write_log(data)
        '''
        for account_data in data["balances"]:
            account = AccountData(
                accountid=account_data["asset"],
                balance=float(account_data["free"]) + float(account_data["locked"]),
                frozen=float(account_data["locked"]),
                gateway_name=self.gateway_name
            )

            if account.balance:
                self.gateway.on_account(account)
        '''
        account_data = data['account']
        self.accountId = account_data['accountId']
        self.publicKeyX = account_data['publicKeyX']
        self.publicKeyY = account_data['publicKeyY']
        self.key = account_data['apiKey']


        self.gateway.write_log("账户信息查询成功")

        self.gateway.write_log("start query_balance")
        self.query_balance()

        self.gateway.write_log("start query_orders")
        self.query_orders()

    def on_query_balance(self, data, request):
        self.gateway.write_log("on_query_balance")
        self.gateway.write_log(data)

        for balance in data['balances']:
            accountId = balance['accountId']
            tokenId = balance['tokenId']
            tokenAmount = balance['totalAmount']
            frozenAmount = balance['frozenAmount']

            #self.gateway.on_account(balance)

        self.gateway.write_log("账户余额查询成功")

    def on_query_orderId(self, data, request):
        self.gateway.write_log("on_query_orderId")
        self.gateway.write_log(data)
        self.gateway.write_log(request)

        tokenId = request.params['tokenId']
        self.orderId[tokenId] = data['orderId']

    def on_query_order(self, data, request):
        """"""
        for d in data:
            dt = datetime.fromtimestamp(d["time"] / 1000)
            time = dt.strftime("%Y-%m-%d %H:%M:%S")

            order = OrderData(
                orderid=d["clientOrderId"],
                symbol=d["symbol"],
                exchange=Exchange.LOOPRING,
                price=float(d["price"]),
                volume=float(d["origQty"]),
                type=ORDERTYPE_LOOPRING2VT[d["type"]],
                direction=DIRECTION_LOOPRING2VT[d["side"]],
                traded=float(d["executedQty"]),
                status=STATUS_LOOPRING2VT.get(d["status"], None),
                time=time,
                gateway_name=self.gateway_name,
            )
            self.gateway.on_order(order)

        self.gateway.write_log("委托信息查询成功")

    def on_query_orders(self, data, request):
        self.gateway.write_log("on_query_orders")
        self.gateway.write_log(data)

        for order in data['orders']:
            hash = order['hash']
            side = order['side']
            market = order['market']

        self.gateway.write_log("所有Orders查询成功")

    def on_query_contract(self, data, request):
        """"""
        self.gateway.write_log("on_query_contract:")
        self.gateway.write_log(data)
        for d in data["tokens"]:

            contract = ContractData(
                symbol=d["symbol"],
                name=d["symbol"],
                exchange=Exchange.LOOPRING,
                size=1,
                address=d['address'],
                decimals=d['decimals'],
                tokenId=d['tokenId'],
                product=Product.SPOT,
                pricetick=0.0,
                history_data=True,
                gateway_name=self.gateway_name,
            )
            self.query_orderId(d['tokenId'])
            self.gateway.on_contract(contract)

            symbol_name_map[contract.symbol] = contract.name

        self.gateway.write_log("合约信息查询成功")

    def on_send_order(self, data, request):
        self.gateway.write_log("on_send_order")
        self.gateway.write_log(data)

        self.orderHash.append(data['orderHash'])
        """"""
        pass

    def on_send_order_failed(self, status_code: str, request: Request):
        """
        Callback when sending order failed on server.
        """
        self.gateway.write_log("on_send_order_failed")
        self.gateway.write_log(status_code)
        self.gateway.write_log(request)
        '''
        order = request.extra
        order.status = Status.REJECTED
        self.gateway.on_order(order)
        '''

        msg = f"委托失败，状态码：{status_code}，信息：{request.response.text}"
        self.gateway.write_log(msg)

    def on_send_order_error(
        self, exception_type: type, exception_value: Exception, tb, request: Request
    ):
        """
        Callback when sending order caused exception.
        """
        self.gateway.write_log("on_send_order_error")
        self.gateway.write_log(exception_value)
        self.gateway.write_log(request)
        order = request.extra
        order.status = Status.REJECTED
        self.gateway.on_order(order)

        # Record exception if not ConnectionError
        if not issubclass(exception_type, ConnectionError):
            self.on_error(exception_type, exception_value, tb, request)

    def on_cancel_order(self, data, request):
        """"""
        self.gateway.write_log("on_cancel_order")
        self.gateway.write_log(data)
        pass

    def on_start_user_stream(self, data, request):
        self.gateway.write_log("on_start_user_stream")
        self.gateway.write_log(data)
        """"""
        self.user_stream_key = data["listenKey"]
        self.keep_alive_count = 0
        url = WEBSOCKET_TRADE_HOST + self.user_stream_key

        self.trade_ws_api.connect(url, self.proxy_host, self.proxy_port)

    def on_keep_user_stream(self, data, request):
        """"""
        pass

    def query_orderId(self, tokenId):
        """"""
        params = {
            "accountId": self.accountId,
            "tokenId": tokenId
        }
        self.add_request(
            method="GET",
            path="/api/v1/orderId",
            callback=self.on_query_orderId,
            params=params
        )

    def query_history(self, req: HistoryRequest):
        """"""
        history = []
        limit = 1000
        start_time = int(datetime.timestamp(req.start))

        while True:
            # Create query params
            params = {
                "symbol": req.symbol,
                "interval": INTERVAL_VT2LOOPRING[req.interval],
                "limit": limit,
                "startTime": start_time * 1000,         # convert to millisecond
            }
            
            # Add end time if specified
            if req.end:
                end_time = int(datetime.timestamp(req.end))
                params["endTime"] = end_time * 1000     # convert to millisecond

            # Get response from server
            resp = self.request(
                "GET",
                "/api/v1/klines",
                data={"security": Security.NONE},
                params=params
            )

            # Break if request failed with other status code
            if resp.status_code // 100 != 2:
                msg = f"获取历史数据失败，状态码：{resp.status_code}，信息：{resp.text}"
                self.gateway.write_log(msg)
                break
            else:
                data = resp.json()
                if not data:
                    msg = f"获取历史数据为空，开始时间：{start_time}"
                    self.gateway.write_log(msg)
                    break

                buf = []
                
                for l in data:
                    dt = datetime.fromtimestamp(l[0] / 1000)    # convert to second

                    bar = BarData(
                        symbol=req.symbol,
                        exchange=req.exchange,
                        datetime=dt,
                        interval=req.interval,
                        volume=float(l[5]),
                        open_price=float(l[1]),
                        high_price=float(l[2]),
                        low_price=float(l[3]),
                        close_price=float(l[4]),
                        gateway_name=self.gateway_name
                    )
                    buf.append(bar)

                history.extend(buf)

                begin = buf[0].datetime
                end = buf[-1].datetime
                msg = f"获取历史数据成功，{req.symbol} - {req.interval.value}，{begin} - {end}"
                self.gateway.write_log(msg)

                # Break if total data count less than limit (latest date collected)
                if len(data) < limit:
                    break

                # Update start time
                start_dt = bar.datetime + TIMEDELTA_MAP[req.interval]
                start_time = int(datetime.timestamp(start_dt))

        return history


class LoopringTradeWebsocketApi(WebsocketClient):
    """"""

    def __init__(self, gateway):
        """"""
        super().__init__()

        self.gateway = gateway
        self.gateway_name = gateway.gateway_name

    def connect(self, url, proxy_host, proxy_port):
        """"""
        self.init(url, proxy_host, proxy_port)
        self.start()

    def on_connected(self):
        """"""
        self.gateway.write_log("交易Websocket API连接成功")

    def on_packet(self, packet: dict):  # type: (dict)->None
        self.gateway.write_log("交易on_packet")
        self.gateway.write_log(packet)
        """"""
        if packet == "ping":
            return

        if packet["e"] == "outboundAccountInfo":
            self.on_account(packet)
        else:
            self.on_order(packet)

    def on_account(self, packet):
        """"""
        for d in packet["B"]:
            account = AccountData(
                accountid=d["a"],
                balance=float(d["f"]) + float(d["l"]),
                frozen=float(d["l"]),
                gateway_name=self.gateway_name
            )
            
            if account.balance:
                self.gateway.on_account(account)

    def on_order(self, packet: dict):
        self.gateway.write_log("交易on_order")
        self.gateway.write_log(packet)
        """"""
        dt = datetime.fromtimestamp(packet["O"] / 1000)
        time = dt.strftime("%Y-%m-%d %H:%M:%S")

        if packet["C"] == "null":
            orderid = packet["c"]
        else:
            orderid = packet["C"]

        order = OrderData(
            symbol=packet["s"],
            exchange=Exchange.LOOPRING,
            orderid=orderid,
            type=ORDERTYPE_LOOPRING2VT[packet["o"]],
            direction=DIRECTION_LOOPRING2VT[packet["S"]],
            price=float(packet["p"]),
            volume=float(packet["q"]),
            traded=float(packet["z"]),
            status=STATUS_LOOPRING2VT[packet["X"]],
            time=time,
            gateway_name=self.gateway_name
        )

        self.gateway.on_order(order)

        # Push trade event
        trade_volume = float(packet["l"])
        if not trade_volume:
            return

        trade_dt = datetime.fromtimestamp(packet["T"] / 1000)
        trade_time = trade_dt.strftime("%Y-%m-%d %H:%M:%S")

        trade = TradeData(
            symbol=order.symbol,
            exchange=order.exchange,
            orderid=order.orderid,
            tradeid=packet["t"],
            direction=order.direction,
            price=float(packet["L"]),
            volume=trade_volume,
            time=trade_time,
            gateway_name=self.gateway_name,
        )
        self.gateway.on_trade(trade)


class LoopringDataWebsocketApi(WebsocketClient):
    """"""

    def __init__(self, gateway):
        """"""
        super().__init__()

        self.gateway = gateway
        self.gateway_name = gateway.gateway_name

        self.ticks = {}

    def connect(self, proxy_host: str, proxy_port: int):
        """"""
        self.proxy_host = proxy_host
        self.proxy_port = proxy_port

        url = WEBSOCKET_DATA_HOST
        self.init(url, self.proxy_host, self.proxy_port)
        self.start()

    def on_connected(self):
        """"""
        self.gateway.write_log("行情Websocket API连接刷新")

    def subscribe(self, req: SubscribeRequest):
        self.gateway.write_log("LoopringDataWebsocketApi subscribe")
        """"""
        '''
        if req.symbol not in symbol_name_map:
            self.gateway.write_log(f"找不到该合约代码{req.symbol}")
            return
        
        # Create tick buf data
        tick = TickData(
            symbol=req.symbol,
            name=symbol_name_map.get(req.symbol, ""),
            exchange=Exchange.LOOPRING,
            datetime=datetime.now(),
            gateway_name=self.gateway_name,
        )
        self.ticks[req.symbol.lower()] = tick
        '''

        # Close previous connection
        #if self._active:
        #    self.stop()
        #    self.join()

        # Create new connection
        channels = {
            "op": "sub",
            "args": [
                # "kline&LRC-ETH&1Hour"
                # ,"depth&LRC-ETH&1",
                # ,"depth10&LRC-ETH&1"
                # ,"trade&LRC-ETH",
                "ticker&LRC-ETH"
            ]
        }
        '''
        for ws_symbol in self.ticks.keys():
            channels.append(ws_symbol + "@ticker")
            channels.append(ws_symbol + "@depth5")
        '''

        # url = WEBSOCKET_DATA_HOST
        # self.init(url, self.proxy_host, self.proxy_port)
        # self.start()
        self.send_packet(channels)

    def on_packet(self, packet):
        self.gateway.write_log("行情on_packet")
        self.gateway.write_log(packet)
        """"""
        if packet == "ping":
            return
        '''
        stream = packet["stream"]
        data = packet["data"]

        symbol, channel = stream.split("@")
        tick = self.ticks[symbol]

        if channel == "ticker":
            tick.volume = float(data['v'])
            tick.open_price = float(data['o'])
            tick.high_price = float(data['h'])
            tick.low_price = float(data['l'])
            tick.last_price = float(data['c'])
            tick.datetime = datetime.fromtimestamp(float(data['E']) / 1000)
        else:
            bids = data["bids"]
            for n in range(5):
                price, volume = bids[n]
                tick.__setattr__("bid_price_" + str(n + 1), float(price))
                tick.__setattr__("bid_volume_" + str(n + 1), float(volume))

            asks = data["asks"]
            for n in range(5):
                price, volume = asks[n]
                tick.__setattr__("ask_price_" + str(n + 1), float(price))
                tick.__setattr__("ask_volume_" + str(n + 1), float(volume))

        if tick.last_price:
            self.gateway.on_tick(copy(tick))
        '''