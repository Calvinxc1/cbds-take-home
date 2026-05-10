from pathlib import Path
import pandas as pd


def load_gdp_data(gdp_file: Path) -> pd.DataFrame:
    gdp_data = pd.read_csv(gdp_file, index_col='Country Code').drop(columns='Country Name')
    gdp_data.columns = gdp_data.columns.astype(int)
    return gdp_data
