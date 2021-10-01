# This function imports a cryptocurrency trading history file in csv format. It is formatted to date and organized by the dates which are in a Timestamp column. It is assumed this file has a Close column with closing price amounts for each Timestamp.

import pandas as pd
from pathlib import Path

def cryptoprices_data_import(path):
    data = pd.read_csv(
        Path(path),
        index_col="Timestamp",
        parse_dates=True,
        infer_datetime_format=True)
    return data