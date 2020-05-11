import fasttext

#trained data path
path = ".\\model\\model_news.bin"

model = fasttext.load_model(path)

#check model info
print(model.words)
print(model.labels)

print(model.predict("全球人類吃素"))
#雞眼用香蕉皮就可以治好