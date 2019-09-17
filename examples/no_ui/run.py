import multiprocessing
from time import sleep
from datetime import datetime, time
from logging import INFO

from vnpy.event import EventEngine
from vnpy.trader.constant import Exchange, Direction, OrderType
from vnpy.trader.object import OrderRequest, CancelRequest
from vnpy.trader.setting import SETTINGS
from vnpy.trader.engine import MainEngine

from vnpy.gateway.loopring import LoopringGateway
from vnpy.gateway.binance import BinanceGateway
from vnpy.app.cta_strategy import CtaStrategyApp
from vnpy.app.cta_strategy.base import EVENT_CTA_LOG

SETTINGS["log.active"] = True
SETTINGS["log.level"] = INFO
SETTINGS["log.console"] = True

loopring_setting = {
    "key": "ZkFS34He1tydFuEcbMI6ksIA4dtqU0ykycI30abtRxkST4VfexIgC4HE3qAuZkHk",
    "secret": "ZkFS34He1tydFuEcbMI6ksIA4dtqU0ykycI30abtRxkST4VfexIgC4HE3qAuZkHk",
    "session_number": 3,
    "address": "0x6b1029C9AE8Aa5EEA9e045E8ba3C93d380D5BDDa",
    "publcKeyX": "3032555699718739012655427019400670474592707110122712334121787061261787356949",
    "publicKeyY": "8244750709992907884325487047280458849269091060072411733281953316881705670521",
    "accountId": 7,
    "ETHTokenId": 0,
    "LRCTokenId": 2
    , "proxy_host": ""
    , "proxy_port": ""
}

binance_setting = {
    "key": "ns0MVIw7mTg1ZLp3wxrpIwaRk9aT4RxXZaIh5Z1Kz7jGTxVpuw9OVsYX4DjkyQVK",
    "secret": "dlYFBM4X23XqiYe1fv9Gzz0veMQlyoPvdzUiMOrbBJ9B9i6klAKijxho9WtdbvWh",
    "session_number": 3,
    "proxy_host": "192.168.1.167",
    "proxy_port": 1080
}


def run_child():
    """
    Running in the child process.
    """
    SETTINGS["log.file"] = True

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    main_engine.add_gateway(LoopringGateway)
    main_engine.add_gateway(BinanceGateway)
    cta_engine = main_engine.add_app(CtaStrategyApp)
    main_engine.write_log("主引擎创建成功")

    log_engine = main_engine.get_engine("log")
    event_engine.register(EVENT_CTA_LOG, log_engine.process_log_event)
    main_engine.write_log("注册日志事件监听")

    main_engine.connect(loopring_setting, "LOOPRING")
    sleep(5)
    # send order
    reqeust_order = OrderRequest(
        symbol="LRC-ETH",
        exchange=Exchange.LOOPRING,
        direction=Direction.LONG,
        price=0.1,
        volume=1.0,
        type=OrderType.LIMIT
    )
    main_engine.send_order(reqeust_order, "LOOPRING")

    '''
    # cancel order
    cancel_order = CancelRequest(
        symbol="LRC-ETH",
        exchange=Exchange.LOOPRING,
        orderid=""
    )
    main_engine.cancel_order(cancel_order, "LOOPRING")
    '''
    # main_engine.connect(binance_setting, "BINANCE")
    main_engine.write_log("连接CTP接口")

    sleep(10)

    '''
    cta_engine.init_engine()
    main_engine.write_log("CTA策略初始化完成")

    cta_engine.init_all_strategies()
    sleep(60)   # Leave enough time to complete strategy initialization
    main_engine.write_log("CTA策略全部初始化")

    cta_engine.start_all_strategies()
    main_engine.write_log("CTA策略全部启动")
    '''

    while True:
        sleep(1)


def run_parent():
    """
    Running in the parent process.
    """
    print("启动CTA策略守护父进程")

    # Chinese futures market trading period (day/night)
    DAY_START = time(8, 45)
    DAY_END = time(15, 30)

    NIGHT_START = time(20, 45)
    NIGHT_END = time(2, 45)

    child_process = None

    while True:
        current_time = datetime.now().time()
        trading = False

        # Check whether in trading period
        '''
        if (
            (current_time >= DAY_START and current_time <= DAY_END)
            or (current_time >= NIGHT_START)
            or (current_time <= NIGHT_END)
        ):
        '''
        trading = True

        # Start child process in trading period
        if trading and child_process is None:
            print("启动子进程")
            child_process = multiprocessing.Process(target=run_child)
            child_process.start()
            print("子进程启动成功")

        # 非记录时间则退出子进程
        if not trading and child_process is not None:
            print("关闭子进程")
            child_process.terminate()
            child_process.join()
            child_process = None
            print("子进程关闭成功")

        sleep(5)


if __name__ == "__main__":
    run_parent()
