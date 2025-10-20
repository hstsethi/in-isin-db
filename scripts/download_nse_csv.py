import requests

def downloadEquityCsv(path="../data/equity.csv"):
    URL = "https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv"
    HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept": "text/csv, */*;q=0.1",
    "Referer": "https://www.nseindia.com/"
}
    resp = requests.get(URL, headers=HEADERS) 
    resp.raise_for_status()
    with open(path, "wb") as f:
        f.write(resp.content)
    return path


