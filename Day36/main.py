import requests
import requests_cache
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

requests_cache.install_cache("api_cache", )

alpha_vantage_api = os.environ.get("ALPHA_API")
news_api = os.environ.get("NEWS_API")

alpha_vantage_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_vantage_api,
}

response = requests.get("https://www.alphavantage.co/query", params=alpha_vantage_params)
response.raise_for_status()
alpha_vantage_data = response.json()

dates = list(alpha_vantage_data["Time Series (Daily)"].keys())
yesterday = dates[0]
day_before_yesterday = dates[1]

yesterday_price = float(alpha_vantage_data["Time Series (Daily)"][yesterday]["1. open"])
day_before_yesterday_price = float(alpha_vantage_data["Time Series (Daily)"][day_before_yesterday]["1. open"])

news_api_params = {
    "q": COMPANY_NAME,
    "sortBy": "popularity",
    "from":day_before_yesterday,
    "to": yesterday,
    "pageSize": 3,
    "apiKey": news_api
}

response = requests.get(url="https://newsapi.org/v2/top-headlines", params=news_api_params)
response.raise_for_status()
news_data = response.json()

change = (yesterday_price - day_before_yesterday_price) / day_before_yesterday_price * 100

if change > 0:
    print(f"${STOCK}: 🔺{round(change, 2)}\n"
          f"Yesterday: {yesterday_price}\n"
          f"Day before yesterday: {day_before_yesterday_price}")
else:
    print(f"${STOCK}: 🔻{round(abs(change), 2)}\n"
          f"Yesterday: {yesterday_price}\n"
          f"Day before yesterday: {day_before_yesterday_price}")

for headlines in news_data["articles"]:
    print(f"From:{headlines["source"]["name"]}\n"
          f"Headline:{headlines["title"]}\n"
          f"Description:{headlines["description"]}\n"
          f"Read more: {headlines["url"]}\n\n")
