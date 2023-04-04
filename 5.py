import pandas as pd
import numpy as np

# Write this function
def mk_df(date_info, aud_usd_info, eur_aud_info):
    date_info_df = pd.DataFrame(date_info, columns=['row_id', 'date'])
    aud_usd_info_df = pd.DataFrame(aud_usd_info, columns=['row_id', 'aud/usd'])
    eur_aud_info_df = pd.DataFrame(eur_aud_info, columns=['row_id', 'eur/aud'])
    merged = pd.merge(date_info_df, aud_usd_info_df, how="outer", on=["row_id"])
    merged2 = pd.merge(merged, eur_aud_info_df, how="outer", on=["row_id"])
    result = pd.DataFrame(merged, columns=['date', 'aud/usd', 'eur/aud'])
    return result
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