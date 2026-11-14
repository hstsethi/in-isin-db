SELECT
    securityname AS name,
    isinnumber AS isin,
    symbol
FROM
    read_csv(
        "https://nsearchives.nseindia.com/content/equities/eq_etfseclist.csv",
        normalize_names = true
    )
