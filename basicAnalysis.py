import pandas as pd
import vectorbt as vbt
import numpy as np
price = vbt.YFData.download('TITAN.NS').get('Close')

fast_ma = vbt.MA.run(price, 10)
slow_ma = vbt.MA.run(price, 50)
entries = fast_ma.ma_crossed_above(slow_ma)
exits = fast_ma.ma_crossed_below(slow_ma)
pf_kwargs = dict(size=np.inf, fees=0.001, freq='1D')

pf = vbt.Portfolio.from_signals(price, entries, exits, init_cash=100000, **pf_kwargs)
print(pf.stats())
pf.plot().show()
