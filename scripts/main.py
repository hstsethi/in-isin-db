from clean_nse_csv import cleanColumns
from download_nse_csv import downloadEquityCsv


def main():
    sec_list_dataset = downloadEquityCsv()
    clean_dataset = cleanColumns(sec_list_dataset)
    clean_dataset.to_csv(sec_list_dataset, index=False)
    return 0


main()
