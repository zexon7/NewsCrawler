import fasttext
import pandas as pd

#data path
path = ".\\segdata\\segData.csv"

#data = pd.read_csv(path, encoding='UTF-8')
#data.iloc[0:int(len(data)*0.8)].to_csv('.\\segdata\\train.txt', header=None, index=None, encoding='utf-8-sig', mode='w')
#data.iloc[int(len(data)*0.8):int(len(data)*0.9)].to_csv('.\\segdata\\test.txt', header=None, index=None, encoding='utf-8-sig', mode='w')

#train_data = ".\\segdata\\train.txt"
#test_data = ".\\segdata\\test.txt"

#train
model = fasttext.train_supervised(path)
#model = fasttext.train_unsupervised(path, model='cbow')
#model = fasttext.train_unsupervised(path, model='skipgram')

#save model
model.save_model(".\\model\\model_news.bin")