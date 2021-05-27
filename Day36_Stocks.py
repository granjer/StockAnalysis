import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY  = YOUR API
STOCK_NEWS_API = YOUR API

STOCK_ENDPOINT = "https://ww6364"w.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = YOUR SID
auth_token = YOUR TOKEN

stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()['Time Series (Daily)']
data_list =[value for (key,value) in data.items()]
yesterday_data=data_list[0]
yesterday_closing_price = yesterday_data['4. close']
# print(yesterday_closing_price)

day_before_yesterday_closing_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_closing_data['4. close']

positive_differnce = abs(float(yesterday_closing_price)-float(day_before_yesterday_closing_price))
up_down = None
if positive_differnce>0:
    up_down = "☝️"
else:
    up_down = " 👇 "

positive_differnce_percentage = round((positive_differnce/float(yesterday_closing_price))*100)

if abs(positive_differnce_percentage) > 1:
    news_params = {
        "apiKey": STOCK_NEWS_API,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles= articles[:3]
    # print(three_articles)

    formatted_articles = [f"{STOCK_NAME} {up_down}{positive_differnce_percentage}% \n Headlines:{article['title']}. \n Description:{article['description']}" for article in three_articles]
    # print(formatted_articles)

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages \
            .create(
            body=article,
            from_='AUTO GENERATED NUMBER',
            to='YOUR NUMBER'
        )
        # print(message.status)
