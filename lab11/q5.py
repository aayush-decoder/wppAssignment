import pandas as pd
# import numpy as np



df = pd.DataFrame({
    'date': pd.to_datetime(['2023-01-01', '2023-01-10', '2023-02-01', '2023-01-01']),
    'artist': ['A', 'A', 'B', 'B'],
    'venue': ['X', 'Y', 'X', 'Y']
})

df['year_month'] = df['date'].dt.to_period('M')

artists = df['artist'].unique()
venues = df['venue'].unique()
artist_venue_pairs = pd.MultiIndex.from_product([artists, venues], names=['artist', 'venue'])



grouped = df.groupby(['year_month', 'artist', 'venue']).size()

year_months = df['year_month'].unique()
index = pd.MultiIndex.from_product([year_months, artist_venue_pairs], names=['year_month', 'artist', 'venue'])

grouped = grouped.reindex(index, fill_value=0)



result = grouped.unstack(['artist', 'venue']).fillna(0).astype(int)
print(result)
