import vectorbt as vbt
import datetime
import numpy as np

with open('symbols.txt', 'r') as file:
    symbols = file.read().splitlines()
for i in range(len(symbols)):
    symbols[i] = symbols[i] + '.NS'

symbols_array = np.array(symbols)
end_date = datetime.datetime.now()

start_date = end_date - datetime.timedelta(days=3)

price = vbt.YFData.download(symbols_array, interval = "1m", start = start_date, end = end_date, missing_index='drop').get('Close')


price.to_csv('price.csv')