import pandas as pd
import requests
import time
import json
import concurrent.futures
from fake_useragent import UserAgent

stock_list = pd.read_csv('/Users/chenti-he/Desktop/stockEngine/stock_list.csv')
historical_data = []

id_date = []

# 年/月/日 迴圈 取得證券代號 合併成 20100101&stockNo=0050 格式
date_year = int(2010)
while date_year < 2021:
    year = str(date_year)
    date_month = [year+'0101', year+'0201', year+'0301', year+'0401', year+'0501', year+'0601',
    year+'0701', year+'0801', year+'0901', year+'1001', year+'1101', year+'1201']
    for month in date_month:
        for i in stock_list.index:
            id_date.append(month+'&stockNo='+str(stock_list.loc[i, 'stock_no']))
    date_year += 1

def get_web_content(id_date):
    
    TWSE_URL = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json'
    # 創建代理IP
    #IP
    ip_data = "152.179.12.86"
    #端口
    port_data = "3128"
    #固定IP格式
    new_data = {
        "http": ip_data + ":" + port_data
    }
    user_agent = UserAgent()
    res = requests.get(TWSE_URL + '&date=' + id_date, headers={ 'user-agent': user_agent.random }, proxies=new_data)

    if res.status_code != 200:
        return None
    else:
        return res.json()
    
def get_data(id_date):
    resp = get_web_content(id_date)
    if resp is None:
        return None
    else:
        if resp['data']:
            for data in resp['data']:
                record = {
                    '日期': data[0],
                    '成交股數': data[1],
                    '成交金額': data[2],
                    '開盤價': data[3],
                    '最高價': data[4],
                    '最低價': data[5],
                    '收盤價': data[6],
                    '漲跌價差': data[7],
                    '成交筆數': data[8]
                }
                historical_data.append(record)
        return historical_data
    time.sleep(60)

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(get_data, id_date)
historical_data = pd.DataFrame(historical_data)
historical_data.to_csv('/Users/chenti-he/Desktop/stockEngine/historical_data.csv')