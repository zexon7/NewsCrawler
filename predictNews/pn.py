import fasttext
import jieba

#trained data path
path = ".\\model\\model_news.bin"

model = fasttext.load_model(path)

def print_results(N, p, r):
    print("N\t" + str(N))
    print("P@{}\t{:.3f}".format(1, p))
    print("R@{}\t{:.3f}".format(1, r))

print_results(*model.test(".\\segdata\\segData.txt"))

#check model info
#print(model.words)
#print(model.labels)

#__label__fake	影片宣稱「人和猴子交配生子」？
#__label__partialError	「吃冷的米飯能抗腸癌」？
n1 = "人猴子交配生子"
n2 = "吃冷米飯抗腸癌"

s1 = jieba.cut(n1, cut_all=False)
d1 = " ".join(s1)
s2 = jieba.cut(n2, cut_all=False)
d2 = " ".join(s2)

#prdict result
print(model.predict(d1))
print(model.predict(d2))