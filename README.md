# in-isin-db

A fresh CSV is fetched from NSE during each run. All columns other than `ISIN NUMBER` and `SYMBOL` are dropped. These column names are further transformed to `isin`, `symbol`. The result is exported in data folder in CSV format.

## Use Case

None of common tools including `=GOOGLEFINANCE`, `=STOCKHISTORY` or Yfinance **support querying through ISIN**. There are some alternatives OpenFIGI API, or converting company name columns to _stock datatype_ in Excel, but none of them work locally or are truly free.


