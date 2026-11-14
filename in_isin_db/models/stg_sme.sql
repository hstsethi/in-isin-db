SELECT
    name_of_company AS name,
    isin_number AS isin,
    symbol
FROM
    read_csv(
        "https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv",
        normalize_names = true
    )
