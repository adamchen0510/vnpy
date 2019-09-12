#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#%%
import sys
import gzip
import os
from typing import List
import pandas as pd

# In[ ]:

#%%

from vnpy.trader.constant import Exchange
from vnpy.trader.object import TickData

if __name__ == "__main__":
    data_dir = sys.argv[1]
    print(f"data dir is {data_dir}")

    file_list = os.listdir(data_dir)
    file_list.sort()
#    df = pd.DataFrame(columns=("exchange_time", "contract", "price", "bs", "amount", "exchange_timestamp", "time", "timestamp"))
    df_index = 0
    for i in range(0, len(file_list)):
        path = os.path.join(data_dir, file_list[i])
        if os.path.isfile(path) and not path.endswith(".gz"):
            #print(f"file is: {path}")
            print(f"file is:{path}")
            #with gzip.open(path, "rb") as f:
            df = pd.read_csv(path, names=["exchange_time", "contract", "price", "bs", "amount", "exchange_timestamp", "time", "timestamp"])

            print(f"df is: {df}")
            '''
            with open(path, "rb") as f:
                for line in f:
                    # print(f"line is: {line}")
                    #lines_tr = bytes.decode(line)
                    lines_tr = line
                    spline = lines_tr.split(",")
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
                    df.insert(df_index
                              ,value=[sptimeT, spline[2], spline[3], spline[4], spline[5], spline[6], spline[7]]
                              ,column=("exchange_time", "contract", "price", "bs", "amount", "exchange_timestamp", "time", "timestamp")
                              ,allow_duplicates=True
                              )
                    df_index = df_index + 1
            f.close()
            df.save
            '''
        df.to_csv('/Users/shengchen/zhubi.csv')