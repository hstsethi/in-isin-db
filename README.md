# in-isin-db

International Security Identification Number(ISIN) is as 12 digit, alphanumeric number that is used to uniquely identify a security.

This is a weekly-updated CSV, SQL database of **all equities listed on NSE** Equity, ETF and SME segment along with their symbol, ISIN, name of company.

You can download the latest database from the Github Actions tab. This method avoids cluttering Git history, releases section and does not require using any API keys or token.
 

## How does it work

This project has been completely refractored to **completely remove Python, Sqlite ecosystem**. Everything now happens via DuckDB and DBT. It fetches the CSV from NSE directly into DuckDB. Slects only required columns, cleans it, and saves the table. There are no intermediary CSV files, ``CREATE TABLE``` boilerplate, no loading via Python then cleaning via DBT. 

For old code see the `python` branch.

## Use Case

- ISIN to Symbol Mapping

None of common tools including `=GOOGLEFINANCE`, `=STOCKHISTORY` or Yfinance support querying through ISIN.

There are some alternatives OpenFIGI API, or converting company name columns to _stock datatype_ in Excel, but none of them work locally or are truly free. 

- Financial Modelling

Especially if you are working from the official disclosure documents. See an example in the parent project [Fund Fundamental Analysis Tools(FFAT)](https://github.com/hstsethi/ffat).

