import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv

stock_no = []
stock_name = []

# 抓取證交所的證券代號 & 名字
url = 'https://isin.twse.com.tw/isin/class_main.jsp?owncode=&stockname=&isincode=&market=1&issuetype=&industry_code=&Page=1&chklike=Y'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
trs = soup.find_all('tr')
for tr in trs:
    # td.getText()才會取到文字，否則會連標籤一起抓
    stock_no.append(tr.find_all('td')[2].getText())
    stock_name.append(tr.find_all('td')[3].getText())

stock_no.pop(0) # 將抬頭移除
stock_name.pop(0) # 將抬頭移除
stock_list = {'stock_no': stock_no,
            'stock_name': stock_name}
stock_list = pd.DataFrame(stock_list)
stock_list.to_csv('/Users/chenti-he/PycharmProjects/stockEngine' + '/stock_list.csv')
