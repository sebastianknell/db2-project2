import pandas as pd
import numpy as np
from nltk import SnowballStemmer, word_tokenize
from nltk.corpus import stopwords
from ast import literal_eval

DATA_FILE = "src/data/articles1.csv"
TERM_INDEX_FILE = "src/data/term-index.txt"
DOC_INDEX_FILE = "src/data/doc-index.txt"
DOC_NORMS_FILE = "src/data/doc-norms.txt"

# Index structure
# term:[(rowID,tf),...] -> df = length of list
def writeIndex(index, filename):
    with open(filename, 'a+', encoding='UTF-8') as file:
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
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            l = line.split()
            if len(l) != 2:
                print("Couldn't read index")
                exit()
            tuples = literal_eval(l[1])
            
            index[l[0]] = dict(tuples)
    return index


def getTermFrequenies(terms):
    tf = {}
    for term in terms:
        if term in tf.keys():
            tf[term] += 1
        else:
            tf[term] = 1
    return tf


def buildIndex():
    file = pd.read_csv(DATA_FILE, encoding='UTF-8')
    stemmer = SnowballStemmer('english')
    stoplist = stopwords.words('english')
    stoplist += ['.', ',', '?', '-', '–', '«', '»',
                  '(', ')', ':', ';', '#', '!', '$', '@', '%', '^', '&', '*', '+', '']
    termIndex = {}
    docNorms = {}
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
        
        tf = getTermFrequenies(words)
        vector = np.array([item[1] for item in tf.items()])
        docNorms[id] = np.linalg.norm(vector)

        # 4. Build termIndex
        # for token in words:
        #     if len(token) > 0 and token in termIndex.keys():
        #         if id in termIndex[token].keys():
        #             termIndex[token][id] += 1
        #         else:
        #             termIndex[token][id] = 1
        #     else:
        #         termIndex[token] = {id: 1}

    # termIndex = dict(sorted(termIndex.items(), key=lambda elem: elem[0]))
    # writeIndex(termIndex, TERM_INDEX_FILE)
    with open(DOC_NORMS_FILE, 'w+') as outFile:
        outFile.writelines(str(docNorms))


def readDocNorms():
    with open(DOC_NORMS_FILE, 'r', encoding='UTF-8') as outFile:
        text = outFile.readline()
    docNorms = literal_eval(text)
    return docNorms

buildIndex()