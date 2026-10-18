import duckdb


def ingest_csv(DB_NAME, DATASETS): 
    # Transformations can technically be done here. It might be more efficient, as only select columns will be read and inserted into database. But lets do in DBT. Just taking advantage of normalize_names().

    with duckdb.connect(DB_NAME) as con:
        for table_name, path in DATASETS.items():
            # Parameters won't work at table name, hence using f-string.
            con.execute(
                f"""
        CREATE OR REPLACE TABLE {table_name} AS
        FROM read_csv($path_param, normalize_names=true)
    """,
                {"path_param": path},
            )


def main():
    DB_NAME = "../data/isin.duckdb"
    DATASETS = {
        "equity": "../data/nse-equity.csv",
        "sme": "../data/nse-sme.csv",
        "etf": "../data/nse-etf.csv",
    }
    ingest_csv(DB_NAME, DATASETS)


main()
