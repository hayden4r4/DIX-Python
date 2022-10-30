import requests
import base64
import json
import datetime as dt
from datetime import date, datetime
import pandas_market_calendars as mcal

keys: str = json.load(open("/mnt/z/API Keys/Finra/FINRA_API_KEY.json"))
keys_concat: str = keys["client"] + ":" + keys["secret"]

auth_bytes: bytes = base64.urlsafe_b64encode(keys_concat.encode("utf-8"))
auth: str = str(auth_bytes, "utf-8")

headers: dict = {"Authorization": "Basic " + auth, "Accept": "application/json"}

today: datetime = date.today()
three_days_ago: datetime = today - dt.timedelta(days=3)
today: str = today.strftime("%Y-%m-%d")
three_days_ago: str = three_days_ago.strftime("%Y-%m-%d")
nyse: mcal.MarketCalendar.factory = mcal.get_calendar("NYSE")
last_market_day: str = nyse.valid_days(start_date=three_days_ago, end_date=today)[
    -1
].strftime("%Y-%m-%d")

params: dict = {
    "limit": 100000,
    "offset": 0,
    "fields": ["totalParQuantity", "shortParQuantity", "tradeReportDate"],
    "compareFilters": [
        {
            "compareType": "EQUAL",
            "fieldName": "tradeReportDate",
            "fieldValue": last_market_day,
        }
    ],
}


def post() -> str:
    """
    Post request to FINRA API
    """
    r: str = requests.post(
        "https://api.finra.org/data/group/otcMarket/name/regShoDaily",
        headers=headers,
        json=params,
    ).json()
    return r


total: int = 0
short: int = 0
n: int = 0
resp: list[dict] = []

while True:
    resp += post()
    for data in resp:
        total += data["totalParQuantity"]
        short += data["shortParQuantity"]
        n += 1
    if n % 5000 != 0:
        break
    params["offset"] += 5000

dix: float = short / total * 100

print(dix)
