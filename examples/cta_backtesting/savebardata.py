#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#%%
import sys
import gzip
import os
from vnpy.app.cta_strategy.backtesting import BacktestingEngine, OptimizationSetting
from datetime import datetime, timedelta
from typing import List
from vnpy.trader.constant import  Interval

# In[ ]:

#%%
from vnpy.trader.constant import Exchange
from vnpy.trader.object import BarData


if __name__ == "__main__":
    data_dir = sys.argv[1]
    print(f"data dir is {data_dir}")

    engine = BacktestingEngine()

    file_list = os.listdir(data_dir)
    file_list.sort()

    start_time = datetime(2018, 1, 1) + timedelta(hours=1)
    start_time_set = True
    open_price_set = False
    open_price = "0"
    high_price = "0"
    low_price = "0"
    close_price = "0"
    volume = "0"
    all_write = False
    for i in range(0, len(file_list)):
        path = os.path.join(data_dir, file_list[i])
        if os.path.isfile(path) and path.endswith(".gz"):
            #print(f"file is: {path}")
            print(f"file is:{path}")
            data: List[BarData] = []
            with gzip.open(path, "rb") as f:
                for line in f:
                    # print(f"line is: {line}")
                    lines_tr = bytes.decode(line)
                    spline = lines_tr.split(",")
                    #'''
                    print(f"split line is: {spline[0]}")
                    print(f"split line is: {spline[1]}")
                    print(f"split line is: {spline[2]}")
                    print(f"split line is: {spline[3]}")
                    print(f"split line is: {spline[4]}")
                    print(f"split line is: {spline[5]}")
                    print(f"split line is: {spline[6]}")
                    print(f"split line is: {spline[7]}")
                    #'''
                    if spline[0] == "time":
                        continue
                    sptime = spline[0].replace("T", " ")
                    sptimeT = sptime.replace("+00:00", "")
                    print(f"sptimeT is: {sptimeT}")
                    print(f"start_time is: {start_time}")
                    try:
                        if datetime.strptime(sptimeT, "%Y-%m-%d %H:%M:%S.%f") >= start_time:
                            if volume > "0":
                                bar = BarData(
                                    symbol="LRC_ETH",
                                    exchange=Exchange.BINANCE,
                                    datetime=start_time - timedelta(hours=1),
                                    interval=Interval.HOUR,
                                    volume=volume,
                                    open_price=open_price,
                                    close_price=close_price,
                                    high_price=high_price,
                                    low_price=low_price,
                                    gateway_name="RQ"
                                )
                            else:
                                bar = BarData(
                                    symbol="LRC_ETH",
                                    exchange=Exchange.BINANCE,
                                    datetime=start_time - timedelta(hours=1),
                                    interval=Interval.HOUR,
                                    volume=volume,
                                    open_price=close_price,
                                    close_price=close_price,
                                    high_price=close_price,
                                    low_price=close_price,
                                    gateway_name="RQ"
                                )
                            print(f"bar: {bar}")
                            data.append(bar)
                            # reset value
                            open_price = "0"
                            high_price = "0"
                            low_price = "0"
                            volume = "0"
                            open_price_set = False
                            start_time = start_time + timedelta(hours=1)
                            all_write = True

                        if not open_price_set:
                            open_price = spline[2]
                            low_price = spline[2]
                            open_price_set = True
                        close_price = spline[2]
                        if spline[2] > high_price:
                            high_price = spline[2]
                        if spline[2] < low_price:
                            low_price = spline[2]
                        volume = str(float(volume) + float(spline[4]))
                        all_write = False
                    except ValueError:
                        print(f"exception: {ValueError}")
            if not all_write:
                if volume > "0":
                    bar = BarData(
                        symbol="LRC_ETH",
                        exchange=Exchange.BINANCE,
                        datetime=start_time - timedelta(hours=1),
                        interval=Interval.HOUR,
                        volume=volume,
                        open_price=open_price,
                        close_price=close_price,
                        high_price=high_price,
                        low_price=low_price,
                        gateway_name="RQ"
                    )
                else:
                    bar = BarData(
                        symbol="LRC_ETH",
                        exchange=Exchange.BINANCE,
                        datetime=start_time - timedelta(hours=1),
                        interval=Interval.HOUR,
                        volume=volume,
                        open_price=close_price,
                        close_price=close_price,
                        high_price=close_price,
                        low_price=close_price,
                        gateway_name="RQ"
                    )
                print(f"bar: {bar}")
                data.append(bar)

            f.close()
            # save to database
            engine.save_bar(data)