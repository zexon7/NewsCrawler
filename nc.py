#News Crawler
#Get news title and url from Google News

from urllib import request
from bs4 import BeautifulSoup
import pandas as pd

url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant"

#set user agent
req = request.Request(url)
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36")
response = request.urlopen(req)
data = response.read().decode("utf-8")

#read data in html format
html = BeautifulSoup(data,"html.parser")

#search for class
titles_data = html.find_all("a",class_="DY5T1d")
titles_source = html.find_all("a",class_="wEwyrc AVN2gc uQIVzc Sksgp")
titles_time = html.find_all("time",class_="WW6dff uQIVzc Sksgp")
#print(titles)
c = 0
'''
for title in titles:
    if c < 2:
        print(title.string)
        print("https://news.google.com"+title.get("href"))
        print("\n")
        c+=1
'''

#put string and url into a list
title_list = [t.string for t in titles_data]
url_list = ["https://news.google.com"+t.get("href")for t in titles_data]
source_list = [s.string for s in titles_source]
title_time = [t.get("datetime") for t in titles_time ]

#create a data frame
df = pd.DataFrame({
    'title': title_list,
    'source': source_list,
    'time': title_time,
    'link': url_list
})

#show full data frame setting
#pd.set_option("display.max_rows", None,'display.max_columns', None,'display.max_colwidth', None)
#print(df.head())

pd.set_option('max_colwidth',100)
display(df.head())