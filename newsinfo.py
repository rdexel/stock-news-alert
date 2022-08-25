import requests
from datetime import date


class NewsInfo:
    def __init__(self):
        self.NEWS_endpoint = 'https://newsapi.org/v2/everything?'
        self.apikey = ''
        self.stock = 'TSLA'
        self.date = str(date.today())
        self.params = {
            'q': self.stock,
            'from': self.date,
            'sortBy': 'popularity',
            'apiKey': self.apikey
        }

    def get_news_info(self):
        response = requests.get(self.NEWS_endpoint, self.params)
        response.raise_for_status()
        data = response.json()
        article_title = data['articles'][0]['title']
        article_description = data['articles'][0]['description']
        article_url = data['articles'][0]['url']
        return article_title, article_description, article_url
