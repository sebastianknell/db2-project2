import pandas as pd
from nltk import SnowballStemmer, word_tokenize
from nltk.corpus import stopwords
from ast import literal_eval

DATA_FILE = "src/data/articles1.csv"
INDEX_FILE = "src/data/index.txt"

# Index structure
# term:[(rowID,tf),...] -> df = length of list
def writeIndex(index, filename):
    with open(filename, 'a+') as file:
        for term, docDict in index.items():
            line = str(term)
            line += ' ['
            for tup in docDict.items():
                line += '('
                line += str(tup[0])
                line += ','
                line += str(tup[1])
                line += '),'
            line += ']'
            line += '\n'
            file.writelines(line)


def readIndex(filename):
    index = {}
    with open(filename, 'r') as file:
        for line in file:
            l = line.split()
            if len(l) != 2:
                print("Couldn't read index")
                exit()
            tuples = literal_eval(l[1])
            index[l[0]] = dict(tuples)
    return index


def buildIndex():
    file = pd.read_csv(DATA_FILE, encoding='UTF-8')
    stemmer = SnowballStemmer('english')
    stoplist = stopwords.words('english')
    stoplist += ['.', ',', '?', '-', '–', '«', '»',
                  '(', ')', ':', ';', '#', '!', '$', '@', '%', '^', '*', '&', '*', '+', '']
    index = {}
    for id, row in file.iterrows():
        text = row['title'] + ' ' + row['content']
        # 1. Tokenize
        words = word_tokenize(text.lower().strip())
        # 2. Filter stopswords
        i = 0
        while i < len(words):
            if words[i] in stoplist:
                words.pop(i)
            else:
                i += 1
        # 3. Stemming
        for i in range(len(words)):
            words[i] = stemmer.stem(words[i])

        # 4. Build index
        for token in words:
            if len(token) > 0 and token in index.keys():
                if id in index[token].keys():
                    index[token][id] += 1
                else:
                    index[token][id] = 1
            else:
                index[token] = {id: 1}

    index = dict(sorted(index.items(), key=lambda elem: elem[0]))
    writeIndex(index, INDEX_FILE)


# buildIndex()
readIndex(INDEX_FILE)