import pandas as pd
from pathlib import Path
df=pd.read_csv(Path(__file__).resolve().parents[1]/'data/climate_data.csv',parse_dates=['date'])
print(df.groupby('city').temperature_c.mean().sort_values(ascending=False).round(2))
print('\nRainfall:')
print(df.groupby('city').rainfall_mm.sum().sort_values(ascending=False).round(2))
