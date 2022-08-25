from stockinfo import StockInfo
from newsinfo import NewsInfo
from sendmessage import SendMessage


COMPANY_NAME = "Tesla Inc"


stock_finder = StockInfo()
news_finder = NewsInfo()

price_change = stock_finder.get_stock_info()
news = news_finder.get_news_info()

send_message = SendMessage

headline = news[0]
brief = news[1]
site = news[2]

indicator = ''
if price_change > 0:
    indicator = '🟢 is up '
elif price_change < 0:
    indicator = '🔴 is down '
elif price_change == 0:
    indicator = '🟡 '

message = f'{COMPANY_NAME} {indicator}{price_change}\n{headline}\n{brief}\n{site}'

send_message.create_message(SendMessage(), message)
