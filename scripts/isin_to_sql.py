import sqlite3
import pandas as pd
def create_table(con):
    con.execute('''CREATE TABLE IF NOT EXISTS isin(isin char(12) PRIMARY KEY, symbol NOT NULL 
  CHECK (length(isin) = 12);''')
    con.commit()

def main():
    DB_NAME = "../data/isin.db"
    ISIN_CSV = "../data/nse-isin.csv"
    con = sqlite3.connect(DB_NAME)
    create_table(con)
    csv = pd.read_csv(ISIN_CSV)
    csv.to_sql("isin", con, index=False, if_exists="append")
    con.close()
main()
