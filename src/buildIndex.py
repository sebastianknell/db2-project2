from nltk.compat import DATA_UPDATES
import pandas as pd
import numpy as np
from nltk import SnowballStemmer, word_tokenize
from nltk.corpus import stopwords

CHUNK_SIZE = 1000
DATA_FILE = "src/data/articles1.csv"
TEMP_FILE = "src/data/temp.txt"
INDEX_FILE = "src/data/index.txt"

# Index structure
# term:[(docID,tf)] -> df = length of list
def writeIndex(index, filename):
    with open(filename, 'a+') as  file:
        for term, docDict in index.items():
            line = str(term)
            line += ':['
            for tup in docDict.items():
                # Remove whitespace between str(tuple)
                tupStr = str(tup)
                tupList = tupStr.split()
                line += str(''.join(tupList))
            line += ']'
            line += '\n'
            file.writelines(line)

def mergeByBlocks():
    return


def buildIndex():
    with pd.read_csv(DATA_FILE, chunksize=CHUNK_SIZE) as reader:
        stemmer = SnowballStemmer('english')
        stoplist = stopwords.words('english')
        stoplist += ['.', '?', '-', '«', '»', ',', '(', ')', ':', ';']
        for chunk in reader:
            # Process chunk
            localIndex = {}
            for id, row in chunk.iterrows():
                text = row['title'] + ' ' + row['content']
                # 1. Tokenize
                words = word_tokenize(text.lower().strip())
                # 2. Filter stopswords
                for w in words:
                    if w in stoplist:
                        words.remove(w)
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
                        localIndex[token] = {id : 1}
                    
            # Write chunck
            writeIndex(localIndex, TEMP_FILE)

buildIndex()