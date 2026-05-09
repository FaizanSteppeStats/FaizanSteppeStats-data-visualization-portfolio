import pandas as pd
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'data/sales_data.csv'
df=pd.read_csv(p,parse_dates=['date'])
print('Total revenue:', round(df.revenue.sum(),2))
print('Total profit:', round(df.profit.sum(),2))
print('\nRevenue by region:')
print(df.groupby('region').revenue.sum().sort_values(ascending=False))
print('\nProfit by category:')
print(df.groupby('category').profit.sum().sort_values(ascending=False))
