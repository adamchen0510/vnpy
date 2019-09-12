#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#%%
import sys
import gzip
import os
from vnpy.app.cta_strategy.backtesting import BacktestingEngine, OptimizationSetting
from datetime import datetime
from typing import List

# In[ ]:

#%%
from vnpy.trader.constant import Exchange
from vnpy.trader.object import TickData

if __name__ == "__main__":
    data_dir = sys.argv[1]
    print(f"data dir is {data_dir}")

    engine = BacktestingEngine()

    file_list = os.listdir(data_dir)
    file_list.sort()
    for i in range(0, len(file_list)):
        path = os.path.join(data_dir, file_list[i])
        if os.path.isfile(path) and path.endswith(".gz"):
            #print(f"file is: {path}")
            print(f"file is:{path}")
            data: List[TickData] = []
            with gzip.open(path, "rb") as f:
                for line in f:
                    # print(f"line is: {line}")
                    lines_tr = bytes.decode(line)
                    spline = lines_tr.split(",")
                    '''
                    print(f"split line is: {spline[0]}")
                    print(f"split line is: {spline[1]}")
                    print(f"split line is: {spline[2]}")
                    print(f"split line is: {spline[3]}")
                    print(f"split line is: {spline[4]}")
                    print(f"split line is: {spline[5]}")
                    print(f"split line is: {spline[6]}")
                    print(f"split line is: {spline[7]}")
                    '''
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
            f.close()
            # save to database
            engine.save_tick(data)