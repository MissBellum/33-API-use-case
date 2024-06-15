import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
KEY = "ARVEN9KGL7QFU40S"
NEWS = "9ceeae86b4534de298e69d9e03bef53a"

request = requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&apikey=ARVEN9KGL7QFU40S")
request.raise_for_status()
price_index = request.json()["Time Series (Daily)"]
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
#  e.g. [new_value for (key, value) in dictionary.items()]
y_stock_price = float(price_index['2023-01-27']['4. close'])
print(y_stock_price)

# TODO 2. - Get the day before yesterday's closing stock price
dby_stock_price = float(price_index['2023-01-26']['4. close'])
print(dby_stock_price)

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
difference_pos = y_stock_price - dby_stock_price
print(difference_pos)

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
difference_perc = (difference_pos / y_stock_price) * 100
print(difference_perc)

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if difference_perc > 5:
    request1 = requests.get(url="https://newsapi.org/v2/everything?q=TSLA&from=2023-01-28&to=2023-01-29&sortBy=popularity&apiKey=9ceeae86b4534de298e69d9e03bef53a")
    request1.raise_for_status()
    articles = request1.json()['articles'][:3]
    print(articles)


# STEP 2: https://newsapi.org/

# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.


# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
# data_list = {key.request1_json["title"]: key.request1_json["description"] for key in request1_json}
# print(data_list)


# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
