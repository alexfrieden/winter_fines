import pandas as pd
df = pd.read_csv('somerville-winter-tickets-2017.csv')
address_count = df.groupby('address').size().sort_values(ascending=False).head(20)
print(address_count)
