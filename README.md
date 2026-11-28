# in-isin-db

International Security Identification Number(ISIN) is as 12 digit, alphanumeric number that is used to uniquely identify a security.

This is a weekly-updated CSV, DuckDB database of **all securities listed on NSE** Equity, ETF and SME segment along with their symbol, ISIN, name of company.

You can download the [latest data from here](https://github.com/hstsethi/in-isin-db/releases/latest/download/nse-isin-data.zip). This URL always points to the latest release.



## How does it work

This project has been completely refactored to **completely remove Python, SQLite ecosystem**. Everything now happens via DuckDB and DBT. It fetches the CSV from NSE directly into DuckDB. Selects only required columns, cleans it, saves the table, and via post-hook exports to CSV. There are no intermediary CSV files, `CREATE TABLE` `COPY TO` boilerplate, no loading via Python then cleaning via DBT. 

For old code see the [python](https://github.com/hstsethi/in-isin-db/tree/python) branch.

~~You can download the latest database from the [Github Actions tab](https://github.com/hstsethi/in-isin-db/actions) artifact section. This method avoids cluttering Git history, releases section and does not require using any API keys or token.~~ But it required being logged into Github to download. I have [raised an issue regarding it](https://github.com/orgs/community/discussions/214200). 
 
## Use Case


- ISIN to Symbol Mapping

None of common tools including `=GOOGLEFINANCE`, `=STOCKHISTORY` or Yfinance support querying through ISIN.

There are some alternatives OpenFIGI API, or converting company name columns to _stock datatype_ in Excel, but none of them work locally or are truly free. 

- Financial Modelling

Especially if you are working from the official disclosure documents. See an example in the parent project [Fund Fundamental Analysis Tools(FFAT)](https://github.com/hstsethi/ffat).

- Number of companies named after a state

For example, see [this gist](https://gist.github.com/hstsethi/53ac47c2e2f9bf6824e01ce22fca8735).
