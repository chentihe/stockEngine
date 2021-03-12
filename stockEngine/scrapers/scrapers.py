from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time
import pandas as pd
# import yfinance as yf
import json
import pymysql
from random import randrange
import concurrent.futures

# 財經網站抽象類別
class Website(ABC):

    def __init__(self, stock_list):
        self.stock_list = stock_list

    @abstractmethod
    def scrape(self): # 爬取股票抽象方法
        pass

    @abstractmethod
    def post_to_mysql(self, stocks): # 將資料存進MySQL方法
        pass

# 鉅亨網
class Anue(Website):

    def scrape(self):

        result = list() #回傳結果

        for stock_no in self.stock_list:

            #取得傳入股票的新聞 一頁最多30筆 limit設30
            response = requests.get(
                f"https://api.cnyes.com/media/api/v1/newslist/TWS%3A{stock_no}%3ASTOCK/symbolNews?page=1&limit=30"
            )

            print('processing stock:' + stock_no)
            # 資料
            news = response.json()['items']['data']

            for new in news:
                
                # 新聞名稱
                stock_no = stock_no
                title = new['title']

                # 新聞詳細內容連結 id
                link = 'https://news.cnyes.com/news/id/' + str(new['newsId'])

                # 新聞發布日期
                time_stamp = new['publishAt']
                struct_time = time.localtime(time_stamp)
                published_at = time.strftime('%Y-%m-%d', struct_time)
                today = datetime.strftime(datetime.now(), '%Y-%m-%d')

                if published_at == today:
                    result.append(
                        tuple([stock_no, title, link, published_at, 'https://login.cnyes.com/logo.svg']))
            sleep_time = randrange(1, 60)
            time.sleep(sleep_time)

        return result

    def post_to_mysql(self, stocks):

        db_settings = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'db': 'stock_engine',
            'charset': 'utf8'
        }

        try:
            conn = pymysql.connect(**db_settings)

            with conn.cursor() as cursor:
                sql = '''INSERT INTO stockEngine_stocknews(
                    stock_no,
                    title,
                    link,
                    published_at,
                    source
                )
                VALUES(%s, %s, %s, %s, %s)'''

                for stock in stocks:
                    cursor.execute(sql, stock)
                conn.commit()
        
        except Exception as e:
            print('Exception', e)
        
        conn.close()

db_settings = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'stock_engine',
    'charset': 'utf8'
}

try:
    conn = pymysql.connect(**db_settings)

    with conn.cursor() as cursor:
        sql = '''SELECT `stock_no` FROM stockEngine_stocklist'''
        cursor.execute(sql)
        stock_list = cursor.fetchall() # Type: Tuple
except Exception as e:
    print('Exception', e)

def anue_scrape(stock_list):
    anue = Anue(stock_list)
    anue.post_to_mysql(anue.scrape())

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(anue_scrape, stock_list)

# def stock_price(stock_no):
#     tickerData = yf.Ticker(str(stock_no) + '.TW')
#     tickerDf = tickerData.history(period='1d')
#     tickerDf.reset_index(level=0, inplace=True)
#     df_json = tickerDf.astype(str).to_json(orient='records', date_format='iso', force_ascii=False)
#     return json.loads(df_json)