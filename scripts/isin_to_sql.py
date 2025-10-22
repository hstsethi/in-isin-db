import sqlite3
import pandas as pd
def create_table(con):
    con.execute('''CREATE TABLE IF NOT EXISTS isin(isin char(12) PRIMARY KEY, symbol NOT NULL);''')
    con.commit()

def main():
    DB_NAME = "../data/isin.db"
    ISIN_CSV = "nse-isin.csv"
    con = sqlite3.connect(DB_NAME)
    create_table(con)
main()
