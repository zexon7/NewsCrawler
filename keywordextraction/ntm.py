#News Text Mining
#Text mining on news websites
#reference https://www.jamleecute.com/%E7%B6%B2%E8%B7%AF%E7%88%AC%E8%9F%B2-web-crawler-text-mining-python/

from urllib import request
from bs4 import BeautifulSoup
import pandas as pd
import jieba
import nltk

#input news article URL
url = ""

#set user agent
req = request.Request(url)
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36")
response = request.urlopen(req)
data = response.read().decode("utf-8")

#read data in html format
html = BeautifulSoup(data,"html.parser")

title = html.find("h1")
print("新聞標題："+title.string)
articleContent = html.find_all("p")

article = []
for p in articleContent:
    article.append(p.text)
articleAll = '\n'.join(article)
#print(articleAll)

#jieba.load_userdict('/user_dict.txt') # 輸入自己字典的路徑

#remove apostrophes/symbol
clean_article = articleAll.replace('[^\w\s]','').replace('\r\n','').replace('／','').replace('【','').replace('】','').replace('《','').replace('》','').replace('，','').replace('。','').replace('「','').replace('」','').replace('（','').replace('）','').replace('(','').replace(')','').replace('！','').replace('？','').replace('、','').replace('▲','').replace('…','').replace('：','')
#print(clean_article)

#避免過多的文字log訊息出現
jieba.setLogLevel(20)
# 設定停用字詞 
#stopwords = {}.fromkeys(["也","但","來","個","再","的","和","是","有","更","會","可能","有何","從","對","就", '\n','越','為','這種','多','越來',' '])
stopwords = [' ']
for word in open('stopwords.txt', 'r', encoding='utf-8'):
    stopwords.append(word.strip())


#mode for reference
'''
Sentence = jieba.cut(clean_article, cut_all=True)
print('全模式'+": "  + "/ ".join(Sentence) + '\n')   
 
Sentence = jieba.cut(clean_article, cut_all=False)
print('精確模式'+": " + "/ ".join(Sentence)+ '\n')  
 
Sentence = jieba.cut(clean_article)  
print('Default為精確模式'+": " + "/ ".join(Sentence)+ '\n')
 
Sentence = jieba.cut_for_search(clean_article)  
print('搜索引擎模式'+": " + "/ ".join(Sentence)+ '\n')
'''

Sentence = jieba.cut_for_search(clean_article) 

#create a python dictionary
hash = {}
for item in Sentence:
    if item in stopwords:
        continue
    if item in hash:
        hash[item] += 1
    else:
        hash[item] = 1

#create a data frame
df = pd.DataFrame.from_dict(hash, orient='index', columns = ['詞頻'])
print(df.head(10).sort_values(by = ['詞頻'], ascending = False))