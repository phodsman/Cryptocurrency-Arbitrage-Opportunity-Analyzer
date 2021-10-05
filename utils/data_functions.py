# Functions for cleaning and refining the data for display.


# This function cleans a data frame that has first been imported using the cyryptoprices_data_import function for analysis and returns it. 
# The data is expected to have a Close column, representing the closing prices for each Timestamp. 
# The Close column will be checked for null values, which will be removed. 
# The Close column will be checked for dollars signs, which will be removed. 
# The Close column will be converted to float values. 
# Duplicate lines will be removed.

import pandas as pd

def data_clean(pricedata):
    if pricedata.isnull().sum() > 0:
        pricedata = pricedata.dropna()
    pricedata.loc[:, "Close"] = pricedata.loc[:, "Close"].str.replace("$", "")
    pricedata.loc[:, "Close"] = pricedata.loc[:, "Close"].astype("float")
    if pricedata.duplicated().sum() > 0:
        pricedata = bitstamp.drop_duplicates()
    return pricedata


# This function returns the data with only the timestamp and close price columns.

def data_slice_close(data):
    data_slice = data.loc[:, "Close"]
    return data_slice

# This function plots a portion of the data sets, taking as input parameters the two cleaned and sliced data sets, the begin date, and end date. It expects bitstamp data to be the first parameter and coinbase data to be the second parameter.

def plot_compare_for_date_range(bitstamp_sliced, coinbase_sliced, start_date, end_date):
    bitstamp_sliced.loc[start_date : end_date].plot(legend=True, figsize=(20,8), title=f"Bitstamp vs Coinbase close prices {start_date} - {end_date}", color="#499C53", label="BTC close price per Bitstamp")
    coinbase_sliced.loc[start_date : end_date].plot(legend=True, figsize=(20,8), color="#2151F5", label="BTC close price per Coinbase")
    return

# This function calculates arbitrage spread for a specific date range. It takes input parameters of the two cleaned and sliced data sets, the begin date, and end date. It expects bitstamp data to be the first parameter and coinbase data to be the second parameter. It returns the spreads for each timestamp.

def arbitrage_spread_for_date_range(bitstamp_sliced, coinbase_sliced, start_date, end_date):
    arbitrage_spread_for_range = bitstamp_sliced.loc[start_date : end_date] - coinbase_sliced.loc[start_date : end_date]
    return arbitrage_spread_for_range
