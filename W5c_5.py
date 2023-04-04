import pandas as pd
import numpy as np

# Write this function
def mk_df(date_info, aud_usd_info, eur_aud_info):
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


    """ Combines the information from different sources to produce a dataframe
        with dates row labels. Row labels must be sorted

        Parameters
        ----------
        date_info : list
            date_info = [(row_id, date)]

        aud_usd_info : list
            aud_usd_info = [(row_id, aud/usd)]


        eur_aud_info : list
            eur_aud_info = [(row_id, eur/aud)]

        Returns
        -------
        df:pandas.DataFrame
        DataFrame with sorted dates as row labels and 'AUD/USD' and 'EUR/AUD' as column labels.
        Missing values are retained and represented by NaN.
        """
    pass


# Sample data for you to develop your function
date_info = [(row_id, date)]
date_info = [
    (11 , '2020-09-08'),
    (70 , '2020-09-09'),
    (99 , '2020-09-10'),
    (4  , '2020-09-11'),
    (7  , '2020-09-14'),
    (100, '2020-09-15'),
]

aud_usd_info = [
    (70 ,  0.7209),
    (4  ,  0.7263),
    (11 ,  0.7280),
    (7  ,  0.7281),
    (100,  0.7285),
]

eur_aud_info = [
    (70 ,  1.6321),
    (4  ,  1.6282),
    (99 ,  1.6221),
    (100,  1.6288),
    (11 ,  1.6232),
]

# Call the function with the sample data
df = mk_df(date_info, aud_usd_info, eur_aud_info)

# Print the resulting DataFrame
print(df)


