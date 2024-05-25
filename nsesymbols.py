import pandas as pd

# Read the CSV file
df = pd.read_csv('ind_nifty50list.csv')

# Extract the list of symbols
symbols = df['Symbol'].tolist()
# Write the list of symbols to a file
with open('symbols.txt', 'w') as file:
    file.write('\n'.join(symbols))

