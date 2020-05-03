#output csv
from urllib import request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import datetime
import time

def createDataFrame(t):
    #put data into a list
    title_list = [p.text.strip() for p in t]
    
    global df
    #check if dataframe exist
    if c == 0:
        df = pd.DataFrame({'title': title_list})
    else:
        df = df.append(pd.DataFrame({'title': title_list}), ignore_index = True)
    
    #check fake
    cond1 = df['title'].str.contains('【錯誤】')
    cond2 = df['title'].str.contains('【部分錯誤】')
    '''
    if title contains 【錯誤】:
        put 'fake'
    elif contains 【部分錯誤】:
        put 'partial error'
    else:
        put 'other'
    '''
    df['tag'] = np.where(cond1, 'fake', np.where(cond2, 'partial error', 'other') )
    
def getData(url):
    #set user agent
    req = request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36")
    response = request.urlopen(req)
    data = response.read().decode("utf-8")

    #read data in html format
    html = BeautifulSoup(data,"html.parser")
    
    #set find area
    t = html.find_all("h3", class_= "article-title")
    
    #create dataframe
    createDataFrame(t) 
    
    #find next page url
    nextpage = html.find("a", string = "下一頁 ›")
    return nextpage["href"]
    time.sleep(5)

def main(): 
    #input news article URL
    #錯誤https://tfc-taiwan.org.tw/articles/category/26/27
    #部分錯誤https://tfc-taiwan.org.tw/articles/category/26/28
    fakeURL = "https://tfc-taiwan.org.tw/articles/category/26/27"
    partial_errorURL = "https://tfc-taiwan.org.tw/articles/category/26/28"
    global c
    c = 0
    for i in range(2):
        #get next page URL from getData function
        fakeURL = "https://tfc-taiwan.org.tw" + getData(fakeURL)   
        c+=1
    
    for i in range(2):
        partial_errorURL = "https://tfc-taiwan.org.tw" + getData(partial_errorURL)
    
    pd.set_option('max_colwidth',100)    
    display(df)
    
    #output csv file
    path = ""
    df.to_csv(path + 'data.csv', encoding='utf_8_sig')

def sleeptime(h,m,s):
    return h*3600 + m*60 + s

#update every 6 hours
second = sleeptime(6,0,0)

while True:  
    main()
    time.sleep(second)
