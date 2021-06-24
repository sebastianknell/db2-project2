import pandas as pd
import numpy as np
from nltk import SnowballStemmer, word_tokenize
from nltk.corpus import stopwords
from ast import literal_eval

CHUNK_SIZE = 2500
DATA_FILE = "src/data/articles1.csv"
TEMP_FILE = "src/data/temp/chunk{}.txt"
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

def mergeByChunks(chunkCount):
    for i in range(0, chunkCount-1, 2):
        index1 = readIndex(TEMP_FILE.format(i))
        index2 = readIndex(TEMP_FILE.format(i+1))
        # Merge


def buildIndex():
    with pd.read_csv(DATA_FILE, chunksize=CHUNK_SIZE, encoding='UTF-8') as reader:
        stemmer = SnowballStemmer('english')
        stoplist = stopwords.words('english')
        stoplist += ['.', ',', '?', '-', '–', '«', '»', '(', ')', ':', ';', '#', '!', '$', '@', '%', '^', '*', '&', '*', '+', '']
        chunkCount = 0
        for chunk in reader:
            chunkCount += 1
            # Process chunk
            localIndex = {}
            for id, row in chunk.iterrows():
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
                    if token in localIndex.keys():
                        if id in localIndex[token].keys():
                            localIndex[token][id] += 1
                        else:
                            localIndex[token][id] = 1
                    else:
                        localIndex[token] = {id: 1}

            # Write chunck
            localIndex = dict(sorted(localIndex.items(), key = lambda elem : elem[0]))
            writeIndex(localIndex, TEMP_FILE.format(chunkCount))
            break
        # mergeByChunks(chunkCount)

# buildIndex()
index = readIndex(TEMP_FILE.format(1))
print(index['tweet'])
