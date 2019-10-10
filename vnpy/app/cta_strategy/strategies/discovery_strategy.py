from collections import defaultdict

from vnpy.app.cta_strategy import (
    CtaTemplate,
    StopOrder,
    TickData,
    BarData,
    TradeData,
    OrderData,
    BarGenerator,
    ArrayManager,
)
from time import sleep


class DiscoveryStrategy(CtaTemplate):
    """"""

    author = "用Python的交易员"

    atr_length = 22
    atr_ma_length = 10
    rsi_length = 5
    rsi_entry = 16
    trailing_percent = 0.8
    fixed_size = 1

    atr_value = 0
    atr_ma = 0
    rsi_value = 0
    rsi_buy = 0
    rsi_sell = 0
    intra_trade_high = 0
    intra_trade_low = 0

    parameters = ["atr_length", "atr_ma_length", "rsi_length",
                  "rsi_entry", "trailing_percent", "fixed_size"]
    variables = ["atr_value", "atr_ma", "rsi_value", "rsi_buy", "rsi_sell"]

    tick_data = defaultdict(TickData)

    def __init__(self, cta_engine, strategy_name, vt_symbol, setting):
        """"""
        super(DiscoveryStrategy, self).__init__(
            cta_engine, strategy_name, vt_symbol, setting
        )
        self.bg = BarGenerator(self.on_bar)
        self.am = ArrayManager()

    def on_init(self):
        """
        Callback when strategy is inited.
        """
        self.write_log("策略初始化")

        self.rsi_buy = 50 + self.rsi_entry
        self.rsi_sell = 50 - self.rsi_entry

        self.load_bar(10)
        # self.load_tick(10)

    def on_start(self):
        """
        Callback when strategy is started.
        """
        self.write_log("策略启动")

    def on_stop(self):
        """
        Callback when strategy is stopped.
        """
        self.write_log("策略停止")

    def on_tick(self, tick: TickData):
        """
        Callback of new tick data update.
        """
        self.tick_data[tick.gateway_name] = tick

        # TODO: do in thread
        if len(self.tick_data) < 2:
            return
        buy_1 = sell_1 = buy_2 = sell_2 = 0.0
        index = 0
        for tick in self.tick_data:
            if index == 0:
                buy_1 = self.tick_data[tick].bid_price_1
                sell_1 = self.tick_data[tick].ask_price_1
            elif index == 1:
                buy_2 = self.tick_data[tick].bid_price_1
                sell_2 = self.tick_data[tick].ask_price_1
            index = index + 1

        self.write_log(
            "sell_1: " + str(sell_1) + " buy_1: " + str(buy_1) + " sell_2: " + str(sell_2) + " buy_2: " + str(buy_2))
        if buy_1 <= 0 or sell_1 <= 0 or buy_2 <= 0 or sell_2 <= 0:
            return

        percent = 0.0
        if sell_1 < buy_2:
            percent = buy_2 / sell_1
        elif sell_2 < buy_1:
            percent = buy_1 / sell_2

        self.write_log("Percent is:" + str(percent))

        # self.bg.update_tick(tick)

    def on_bar(self, bar: BarData):
        """
        Callback of new bar data update.
        """
        self.cancel_all()

        am = self.am
        am.update_bar(bar)
        if not am.inited:
            return

        atr_array = am.atr(self.atr_length, array=True)
        self.atr_value = atr_array[-1]
        self.atr_ma = atr_array[-self.atr_ma_length:].mean()
        self.rsi_value = am.rsi(self.rsi_length)

        if self.pos == 0:
            self.intra_trade_high = bar.high_price
            self.intra_trade_low = bar.low_price

            if self.atr_value > self.atr_ma:
                if self.rsi_value > self.rsi_buy:
                    self.buy(bar.close_price + 5, self.fixed_size)
                elif self.rsi_value < self.rsi_sell:
                    self.short(bar.close_price - 5, self.fixed_size)

        elif self.pos > 0:
            self.intra_trade_high = max(self.intra_trade_high, bar.high_price)
            self.intra_trade_low = bar.low_price

            long_stop = self.intra_trade_high * \
                        (1 - self.trailing_percent / 100)
            self.sell(long_stop, abs(self.pos), stop=True)

        elif self.pos < 0:
            self.intra_trade_low = min(self.intra_trade_low, bar.low_price)
            self.intra_trade_high = bar.high_price

            short_stop = self.intra_trade_low * \
                         (1 + self.trailing_percent / 100)
            self.cover(short_stop, abs(self.pos), stop=True)

        self.put_event()

    def on_order(self, order: OrderData):
        """
        Callback of new order data update.
        """
        pass

    def on_trade(self, trade: TradeData):
        """
        Callback of new trade data update.
        """
        self.put_event()
        self.send_order()

    def on_stop_order(self, stop_order: StopOrder):
        """
        Callback of stop order update.
        """
        pass
