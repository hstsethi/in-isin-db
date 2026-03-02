import pandas as pd


def clean_columns(sec_list_dataset, enc="utf-8"):
    sec = pd.read_csv(sec_list_dataset, encoding=enc)
    sec.columns = (
        sec.columns.str.strip().str.lower().str.replace(" ", "_")
    )  # some of them contain leading whitespace
    # SME columns already have _ 

    sec = sec.rename(columns={
        "isin_number": "isin",
        "securityname": "name_of_company", # for ETF
        "isinnumber": "isin" # for ETF
    })
    sec = sec[["symbol", "isin", "name_of_company"]]
    return sec
