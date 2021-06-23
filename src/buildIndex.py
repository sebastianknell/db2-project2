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
                    localIndex[token].add(id)
                else:
                    localIndex[token] = set([id])
        # Write chunck

        # Merge all chunks
