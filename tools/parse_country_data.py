import pandas as pd

def parse_country_data(gdp_data: pd.DataFrame, enroll_data: pd.DataFrame) -> pd.DataFrame:
    full_country_set = tuple(set(gdp_data.index) | set(enroll_data['countrycode'].unique()))
    country_codes = pd.DataFrame(index=full_country_set).sort_index()

    country_codes['gdp_avail'] = country_codes.index.isin(gdp_data.index)
    country_codes['enroll_avail'] = country_codes.index.isin(enroll_data['countrycode'])
    country_codes['full_avail'] = country_codes['gdp_avail'] & country_codes['enroll_avail']

    return country_codes
