import twstock

import pandas as pd
import requests
from io import StringIO
import time
from MooseStockLib import revenue
#%%
def monthly_report(year, month):
    
    # 假如是西元，轉成民國
    if year > 1990:
        year -= 1911
    
    url = 'http://mops.twse.com.tw/nas/t21/sii/t21sc03_'+str(year)+'_'+str(month)+'_0.html'
    if year <= 98:
        url = 'http://mops.twse.com.tw/nas/t21/sii/t21sc03_'+str(year)+'_'+str(month)+'.html'
    
    # 偽瀏覽器
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
    # 下載該年月的網站，並用pandas轉換成 dataframe
    r = requests.get(url, headers=headers)
    r.encoding = 'big5'
    html_df = pd.read_html(StringIO(r.text))
    
    # 處理一下資料
    if html_df[0].shape[0] > 500:
        df = html_df[0].copy()
    else:
        df = pd.concat([df for df in html_df if df.shape[1] <= 11])
    df = df[list(range(0,10))]
    column_index = df.index[(df[0] == '公司代號')][0]
    df.columns = df.iloc[column_index]
    df['當月營收'] = pd.to_numeric(df['當月營收'], 'coerce')
    df = df[~df['當月營收'].isnull()]
    df = df[df['公司代號'] != '合計']
    
    # 偽停頓
    time.sleep(5)
    return df


stock = twstock.Stock('2330')
bfp = twstock.BestFourPoint(stock)
df = monthly_report(2018,8)
#%%
'''
print ('bfp.best_four_point_to_buy')
print (bfp.best_four_point_to_buy())

print ('bfp.best_four_point_to_sell')
print (bfp.best_four_point_to_sell())

print ('bfp.best_four_point')
print (bfp.best_four_point())
print (stock.moving_average(stock.price,3))
print ('--------')
print (stock.moving_average(stock.price,6))
#print (stock.price[-5:])   # 近五日之收盤價
'''
revenue.testModule("Mooseeeee!!!00")
