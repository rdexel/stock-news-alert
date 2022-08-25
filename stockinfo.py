import requests


class StockInfo:
    def __init__(self):
        self.STOCK_endpoint = 'https://www.alphavantage.co/query?'
        self.apikey = ''
        self.stock = 'TSLA'
        self.function = 'TIME_SERIES_DAILY'
        self.params = {
            'function': self.function,
            'symbol': self.stock,
            'apikey': self.apikey
        }

    def get_stock_info(self):
        response = requests.get(self.STOCK_endpoint, self.params)
        response.raise_for_status()
        data = response.json()
        date = list(data['Time Series (Daily)'])[0]
        stock_open_price = float(data['Time Series (Daily)'][f'{date}']['1. open'])
        stock_close_price = float(data['Time Series (Daily)'][f'{date}']['4. close'])
        stock_change = round((((stock_close_price - stock_open_price) / stock_open_price) * 100), 2)
        return stock_change

