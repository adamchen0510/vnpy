#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#%%
from vnpy.app.cta_strategy.backtesting import BacktestingEngine, OptimizationSetting
from vnpy.app.cta_strategy.strategies.atr_rsi_strategy import (
    AtrRsiStrategy,
)
from datetime import datetime


# In[ ]:


#%%
from vnpy.app.cta_strategy.strategies.boll_channel_strategy import BollChannelStrategy

engine = BacktestingEngine()
print(f"start time: {datetime(2018, 1, 1)}")
print(f"end   time: {datetime(2019, 8, 30)}")
engine.set_parameters(
    vt_symbol="LRC_ETH.BINANCE",
    interval="1m",
    start=datetime(2018, 1, 1),
    end=datetime(2019, 8, 30),
    rate=0.3/10000,
    slippage=0.2,
    size=300,
    pricetick=0.2,
    capital=1_000_000,
    #mode=1,
)
engine.add_strategy(AtrRsiStrategy, {})
#engine.add_strategy(BollChannelStrategy, {})


# In[ ]:


#%%
engine.load_data()
engine.run_backtesting()
df = engine.calculate_result()
engine.calculate_statistics()
engine.show_chart()


# In[ ]:


#setting = OptimizationSetting()
#setting.set_target("sharpe_ratio")
#setting.add_parameter("atr_length", 3, 39, 1)
#setting.add_parameter("atr_ma_length", 10, 30, 1)

#engine.run_ga_optimization(setting)

