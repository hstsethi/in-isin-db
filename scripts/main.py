from download_nse_csv import download_nse_CSV


def main():
    download_nse_CSV(
        "../data/nse-sme.csv",
        "https://nsearchives.nseindia.com/emerge/corporates/content/SME_EQUITY_L.csv",
    )

    download_nse_CSV(
        "../data/nse-equity.csv",
        "https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv",
    )

    download_nse_CSV(
        "../data/nse-etf.csv",
        "https://nsearchives.nseindia.com/content/equities/eq_etfseclist.csv",
    )
    return 0


main()
