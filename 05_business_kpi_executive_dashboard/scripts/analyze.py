import pandas as pd
from pathlib import Path
df=pd.read_csv(Path(__file__).resolve().parents[1]/'data/business_kpis.csv',parse_dates=['month'])
print('Total revenue:', round(df.revenue.sum(),2))
print('Total orders:', df.orders.sum())
print('Average conversion:', round(df.conversion_rate_percent.mean(),2),'%')
print('Average retention:', round(df.retention_rate_percent.mean(),2),'%')
