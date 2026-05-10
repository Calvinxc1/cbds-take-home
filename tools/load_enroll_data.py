from pathlib import Path
import pandas as pd


def load_enroll_data(enroll_file: Path) -> pd.DataFrame:
    enroll_data = pd.read_csv(enroll_file, low_memory=False)
    enroll_mask = enroll_data['students5_estimated'].notnull()
    enroll_data = enroll_data.loc[enroll_mask]
    return enroll_data
