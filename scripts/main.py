from clean_nse_csv import clean_columns
from download_nse_csv import download_nse_CSV


def setup_SME():
    SME_list_dataset = download_nse_CSV(
        "../data/nse-sme.csv",
        "https://nsearchives.nseindia.com/content/equities/SME_EQUITY_L.csv",
    )
    clean_SME_dataset = clean_columns(SME_list_dataset)
    clean_SME_dataset.to_csv(SME_list_dataset, index=False)


def setup_equity():
    sec_list_dataset = download_nse_CSV(
        "../data/nse-equity.csv",
        "https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv",
    )

    clean_dataset = clean_columns(sec_list_dataset)
    clean_dataset.to_csv(sec_list_dataset, index=False)


def main():
    setup_SME()
    setup_equity()
    return 0


main()
