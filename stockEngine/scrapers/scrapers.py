from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time

# 財經網站抽象類別
class Website(ABC):

    def __init__(self, stock_no):
        self.stock_no = stock_no

    @abstractmethod
    def scrape(self): #爬取股票抽象方法
        pass

# 鉅亨網
class Anue(Website):

    def scrape(self):

        result = [] #回傳結果

        if self.stock_no:

            #取得傳入股票的新聞
            response = requests.get(
                f"https://api.cnyes.com/media/api/v1/newslist/TWS%3A{self.stock_no}%3ASTOCK/symbolNews?page=1&limit=10"
            )

            # 資料
            news = response.json()['items']['data']

            for new in news:
                
                # 新聞名稱
                title = new['title']

                # 新聞詳細內容連結 id
                link = 'https://news.cnyes.com/news/id/' + str(new['newsId'])

                # 新聞發布日期
                time_stamp = new['publishAt']
                struct_time = time.localtime(time_stamp)
                published_at = time.strftime('%Y-%m-%d', struct_time)

                result.append(
                    dict(title=title, link=link, published_at=published_at,
                    source='https://login.cnyes.com/logo.svg'))
        return result