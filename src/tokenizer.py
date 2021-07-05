from nltk import SnowballStemmer, word_tokenize
from nltk.corpus import stopwords

stoplist = stopwords.words('english')
stoplist += ['.', ',', '?', '-', '–', '«', '»',
             '(', ')', ':', ';', '#', '!', '$', '@', '%', '^', '&', '*', '+', '']
stemmer = SnowballStemmer('english')

def parse(text):
    words = word_tokenize(text.lower().strip())
    i = 0
    while i < len(words):
        if words[i] in stoplist:
            words.pop(i)
        else:
            i += 1
    for i in range(len(words)):
        words[i] = stemmer.stem(words[i])
    return words
