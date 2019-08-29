#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#%%
import sys
from vnpy.app.cta_strategy.backtesting import BacktestingEngine, OptimizationSetting
from datetime import datetime
from typing import List

# In[ ]:

#%%
from vnpy.trader.constant import Exchange
from vnpy.trader.object import TickData

if __name__ == "__main__":
    data_file = sys.argv[1]
    print(f"data file is {data_file}")

    engine = BacktestingEngine()
    data: List[TickData] = []

    with open(data_file, 'r') as f:
        for line in f:
            print(f"line is: {line}")
            spline = line.split(",")
            print(f"split line is: {spline[0]}")
            print(f"split line is: {spline[1]}")
            print(f"split line is: {spline[2]}")
            print(f"split line is: {spline[3]}")
            print(f"split line is: {spline[4]}")
            print(f"split line is: {spline[5]}")
            print(f"split line is: {spline[6]}")
            print(f"split line is: {spline[7]}")
            if spline[0] == "time":
                continue
            sptime = spline[0].replace("T", " ")
            sptimeT = sptime.replace("Z", "")
            tick = TickData(
                symbol="LRC_ETH",
                exchange=Exchange.BINANCE,
                datetime=sptimeT,
                last_price=spline[2],
                last_volume=spline[3],
                ask_price_1=spline[4],
                ask_volume_1=spline[5],
                bid_price_1=spline[6],
                bid_volume_1=spline[7],
                gateway_name="RQ"
            )
            data.append(tick)
    engine.save_tick(data)