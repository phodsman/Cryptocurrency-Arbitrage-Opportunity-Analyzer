# Functions for cleaning and refining the data for display.


# This function cleans a data frame that has first been imported using the cyryptoprices_data_import function for analysis and returns it. 
# The data is expected to have a Close column, representing the closing prices for each Timestamp. 
# The Close column will be checked for null values, which will be removed. 
# The Close column will be checked for dollars signs, which will be removed. 
# The Close column will be converted to float values. 
# Duplicate lines will be removed.

import pandas as pd

def data_clean(pricedata):
    if pricedata.isnull().sum().sum() > 0:
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