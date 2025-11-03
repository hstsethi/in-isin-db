# in-isin-db

International Security Identification Number(ISIN) is as 12 digit, alphanumeric number that is used to uniquely identify a security.

This is a weekly-updated CSV, SQL database of **all securities listed on NSE** along with their symbol, ISIN. 

You can download the latest database from the Github Actions tab. This method avoids cluttering Git history, releases section and does not require using any API keys or token.
 

## How does it work

A fresh CSV is fetched from NSE during each run. All columns other than `ISIN NUMBER` and `SYMBOL` are dropped. These column names are further transformed to `isin`, `symbol`. The result is exported in data folder in CSV format. 

If you wish to export it as SQLite, you can use the `isin_to_sql.py` script. The advantage of using this script over Pandas `to.sql()` is that it will explictly create a strict schema before exporting.

## Use Case

None of common tools including `=GOOGLEFINANCE`, `=STOCKHISTORY` or Yfinance **support querying through ISIN**. There are some alternatives OpenFIGI API, or converting company name columns to _stock datatype_ in Excel, but none of them work locally or are truly free.

There are some other databases on Github, but most of them are outdated, scrapped/fetched from a non-free service, and bloated with lot of other unecessary information.
