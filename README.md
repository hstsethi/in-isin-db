# in-isin-db

A fresh CSV is fetched from NSE during each run. All columns other than `ISIN NUMBER` and `SYMBOL` are dropped. These column names are further transformed to `isin`, `symbol`. The result is exported in data folder in CSV format. 

If you wish to export it as SQLite, you can use the `isin_to_sql.py` script. The advantage of using this script over Pandas `to.sql()` is that it will explictly create a strict schema before exporting.

## Use Case

None of common tools including `=GOOGLEFINANCE`, `=STOCKHISTORY` or Yfinance **support querying through ISIN**. There are some alternatives OpenFIGI API, or converting company name columns to _stock datatype_ in Excel, but none of them work locally or are truly free.


