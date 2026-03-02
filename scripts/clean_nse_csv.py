import pandas as pd


def clean_columns(sec_list_dataset):
    sec = pd.read_csv(sec_list_dataset)
    sec.columns = (
        sec.columns.str.strip().str.lower().str.replace(" ", "_")
    )  # some of them contain leading whitespace
    # SME columns already have _ 

    sec = sec.rename(columns={"isin_number": "isin"})
    sec = sec[["symbol", "isin", "name_of_company"]]
    return sec
