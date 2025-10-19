# in-isin-db

A fresh CSV is fetched from NSE during each run. All columns other than `ISIN NUMBER` and `SYMBOL` are dropped. These column names are further transformed to `isin`, `symbol`. The result is exported in data folder in CSV format.
