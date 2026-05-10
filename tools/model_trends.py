import pandas as pd
from statsmodels.tsa.api import Holt
import warnings
from typing import Iterable


def model_trends(country_codes: Iterable[str], gdp_data: pd.DataFrame, enroll_data: pd.DataFrame,
                 alpha: float = 0.8, beta: float = 0.2) -> dict[str, pd.DataFrame]:
    trends = {}
    for country_code in country_codes.index[country_codes['full_avail']]:
        country_gdp = gdp_data.loc[country_code].astype(float)
        country_gdp = country_gdp.loc[country_gdp.first_valid_index():country_gdp.last_valid_index()]
        if country_gdp.isnull().sum() > 0:
            raise Exception(f"Code {country_code} has interior nan values in gdp data, halting.")

        country_enroll = enroll_data.loc[country_code].fillna(0).astype(float)

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            model_gdp = Holt(country_gdp, initialization_method='estimated') \
                .fit(smoothing_level=alpha, smoothing_trend=beta, optimized=False)

            model_enroll = Holt(country_enroll, initialization_method='estimated') \
                .fit(smoothing_level=alpha, smoothing_trend=beta, optimized=False)

        trends[country_code] = pd.concat([
            model_gdp.trend.rename('gdp'),
            model_enroll.trend.rename('enroll'),
        ], axis=1).sort_index()

    return trends
