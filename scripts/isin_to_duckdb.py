import duckdb


def ingest_csv():
    # Transformations can technically take place here. It might be more efficient, as only select columns will be read and inserted into database. But lets do in DBT.
    with duckdb.connect(DB_NAME) as con:
        for table_name, path in DATASETS.items():
            # Parameters won't work at table name, hence using f-string.
            con.execute(
                f"""
        CREATE OR REPLACE TABLE {table_name} AS
        FROM read_csv($path_param)
    """,
                {"path_param": path},
            )


def main():
    DB_NAME = "../data/isin.db"
    DATASETS = {
        "equity": "../data/nse-equity.csv",
        "sme": "../data/nse-sme.csv",
        "etf": "../data/nse-etf.csv",
    }
    ingest_csv()


main()
