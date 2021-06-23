import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk import SnowballStemmer
import pandas as pd

BLOCK_SIZE = 1000


with pd.read_csv("src/data/articles1.csv", chunksize=BLOCK_SIZE) as reader:
    stemmer = SnowballStemmer('english')
    stoplist = stopwords.words('english')
    stoplist += ['.', '?', '-', '«', '»', ',', '(', ')', ':', ';']
    for chunk in reader:
        # Process chunk
        for index, row in chunk.iterrows():
            text = row['title'] + ' ' + row['content']
            # 1. Tokenize
            words = nltk.word_tokenize(text.lower().strip())
            # 2. Filter stopswords
            for w in words:
                if w in stoplist:
                    words.remove(w)
            # 3. Stemming
            for i in range(len(words)):
                words[i] = stemmer.stem(words[i])
            
            # Build index


