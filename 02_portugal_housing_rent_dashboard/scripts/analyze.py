import pandas as pd
from pathlib import Path
df=pd.read_csv(Path(__file__).resolve().parents[1]/'data/portugal_rent_data.csv',parse_dates=['month'])
print(df.groupby('city').rent_eur.mean().sort_values(ascending=False).round(2))
print('\nRent per sqm:')
print(df.groupby('city').rent_per_sqm.mean().sort_values(ascending=False).round(2))
