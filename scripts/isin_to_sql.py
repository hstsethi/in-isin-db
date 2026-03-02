import sqlite3
import pandas as pd


def create_table(con):
    con.execute("""CREATE TABLE IF NOT EXISTS isin (
    isin CHAR(12) PRIMARY KEY,
    symbol TEXT NOT NULL,
    name_of_company TEXT NOT NULL,
    CHECK (length(isin) = 12)
    );""")
    con.commit()


def main():
    DB_NAME = "../data/nse-equity.db"
    ISIN_CSV = "../data/nse-equity.csv"
    con = sqlite3.connect(DB_NAME)
    create_table(con)
    csv = pd.read_csv(ISIN_CSV)
    csv.to_sql("isin", con, index=False, if_exists="append")
    con.close()


main()
