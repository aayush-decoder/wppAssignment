import pandas as pd

asking_prices = pd.Series([5000, 7000, 6000, 9000, 12000])
fair_prices = pd.Series([5500, 7500, 5800, 9500, 12500])

good_deals = asking_prices < fair_prices

indices = good_deals[good_deals].index.tolist()

print(indices)
