import pandas as pd


def cleanColumns(sec_list_dataset):
    sec = pd.read_csv(sec_list_dataset)
    sec.columns = sec.columns.str.strip().str.lower()  # Snake Casing is not necessary as required cols are all single word but some of them contain leading whitespace
    sec = sec.rename(columns={"isin number": "isin"})
    sec = sec.rename(columns={"name of company": "name_of_company"})
    sec = sec[["symbol", "isin", "name_of_company"]]
    return sec
