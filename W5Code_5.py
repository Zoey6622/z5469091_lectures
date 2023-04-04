import pandas as pd
import numpy as np

# Write this function
# Create DataFrame with date_info
df = pd.DataFrame(date_info, columns=['row_id', 'date'])

# Merge AUD/USD and EUR/AUD information
aud_usd_df = pd.DataFrame(aud_usd_info, columns=['row_id', 'AUD/USD'])
eur_aud_df = pd.DataFrame(eur_aud_info, columns=['row_id', 'EUR/AUD'])
merge_df = pd.merge(aud_usd_df, eur_aud_df, on='row_id', how='outer')

# Merge with date_info DataFrame
df = pd.merge(df, merge_df, on='row_id', how='outer')

# Sort by date
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date').reset_index(drop=True)

return df
    pass


# Sample data for you to develop your function
# date_info = [(row_id, date)]
date_info = [
    (11 , '2020-09-08'),
    (70 , '2020-09-09'),
    (99 , '2020-09-10'),
    (4  , '2020-09-11'),
    (7  , '2020-09-14'),
    (100, '2020-09-15'),
    ]

# aud_usd_info = [(row_id, aud/usd)]
aud_usd_info = [
    (70 ,  0.7209),
    (4  ,  0.7263),
    (11 ,  0.7280),
    (7  ,  0.7281),
    (100,  0.7285),
]


# eur_aud_info = [(row_id, eur/aud)]
eur_aud_info = [
    (70 ,  1.6321),
    (4  ,  1.6282),
    (99 ,  1.6221),
    (100,  1.6288),
    (11 ,  1.6232),
    ]

df = mk_df(date_info, aud_usd_info, eur_aud_info)
print(df)