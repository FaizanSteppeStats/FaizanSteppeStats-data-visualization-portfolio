import pandas as pd
from pathlib import Path
df=pd.read_csv(Path(__file__).resolve().parents[1]/'data/streaming_content_data.csv',parse_dates=['publish_date'])
print(df.groupby('platform').views.sum().sort_values(ascending=False))
print('\nGenre views:')
print(df.groupby('genre').views.sum().sort_values(ascending=False))
