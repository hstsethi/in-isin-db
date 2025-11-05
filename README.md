# in-isin-db

International Security Identification Number(ISIN) is as 12 digit, alphanumeric number that is used to uniquely identify a security.

This is a weekly-updated CSV, SQL database of **all equities listed on NSE** Equity and SME segment along with their symbol, ISIN, name of company.

You can download the latest database from the Github Actions tab. This method avoids cluttering Git history, releases section and does not require using any API keys or token.
 

## How does it work

A fresh CSV is fetched from NSE during each run. All columns other than `ISIN NUMBER`, `NAME OF COMPANY` and `SYMBOL` are dropped. These column names are further transformed to `isin`, `symbol`. The result is exported in data folder in CSV format. 

The `isin_to_sql.py` script can be used to export to SQL. The advantage of using this script over Pandas `to.sql()` is that it will explictly create a strict schema before exporting.

There are some other databases on Github. But most of them are outdated, scrapped/fetched from a non-free service, store huge CSVs in Git repo, and are bloated with lot of other unecessary information.

## Use Case

- ISIN to Symbol Mapping

None of common tools including `=GOOGLEFINANCE`, `=STOCKHISTORY` or Yfinance support querying through ISIN.

There are some alternatives OpenFIGI API, or converting company name columns to _stock datatype_ in Excel, but none of them work locally or are truly free. 

- Financial Modelling

Especially if you are working from the official disclosure documents. See an example in the parent project [Fund Fundamental Analysis Tools(FFAT)](https://github.com/hstsethi/ffat).

