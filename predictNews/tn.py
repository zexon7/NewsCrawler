import fasttext

#data path
path = ".\\segdata\\segData.txt"

#train
model = fasttext.train_supervised(path)
#model = fasttext.train_unsupervised(path, model='cbow')
#model = fasttext.train_unsupervised(path, model='skipgram')

#save model
model.save_model(".\\model\\model_news.bin")

'''
#check the model effectiveness
def print_results(N, p, r):
    print("N\t" + str(N))
    print("P@{}\t{:.3f}".format(1, p))
    print("R@{}\t{:.3f}".format(1, r))

print_results(*model.test(path))
'''
def print_results(N, p, r):
    print("N\t" + str(N))
    print("P@{}\t{:.3f}".format(1, p))
    print("R@{}\t{:.3f}".format(1, r))

print_results(*model.test(path))