import pandas as pd


def sum_enroll_data(enroll_data: pd.DataFrame, agg_field: str) -> pd.DataFrame:
    enroll_sum = enroll_data.groupby(['countrycode', 'year'])[agg_field].sum().reset_index() \
        .rename(columns={'countrycode': 'Country Code', 'year': 'Year', agg_field: 'value'})

    enroll_sum['Year'] = enroll_sum['Year'].astype(int)

    enroll_sum = enroll_sum.pivot(index='Country Code', columns='Year', values='value')

    return enroll_sum
