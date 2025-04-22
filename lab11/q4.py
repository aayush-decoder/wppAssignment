import pandas as pd
import numpy as np

data = {
    'John': [True, False, True, False, False, True, False, True, False, False],
    'Judy': [True, False, False, False, True, True, False, False, True, False]
}

df = pd.DataFrame(data)

party = df['John'] & df['Judy']

df['days_til_party'] = np.nan

next_party = None

for i in reversed(range(len(df))):
    if party[i]:
        next_party = 0
        df.at[i, 'days_til_party'] = 0
    elif next_party is not None:
        next_party += 1
        df.at[i, 'days_til_party'] = next_party

df['days_til_party'] = df['days_til_party'].astype('Int64')

print(df)
