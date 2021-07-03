import pandas as pd
import numpy as np
import nltk
from nltk import SnowballStemmer, word_tokenize
from nltk.corpus import stopwords
#import buildIndex

def getFrequency(term):
    result = []
    for key in term:
        result.append(term[key])
    return result

def getLogFreq(tf):
    logFreq_vec = []
    for i in tf:
        if( i > 0):
            logFreq_vec.append(1 + math.log10(i))
        else:
            logFreq_vec.append(0)
    return logFreq_vec

def getDocFrequency(frequencies):
    return len(frequencies)

def getIDF(df, n):
    return np.log10(n/df)

def getTF_IDF(tf,idf):
    tf_idf_vec = []
    for i in tf:
        tf_idf_vec.append(i * idf)
    return tf_idf_vec

def getNorm(terms):
    norm = 0
    for tf in terms:
        norm += (tf**2)
    return np.sqrt(norm)

#####################################################################

def parse(query):
    words = nltk.word_tokenize(query.lower())
    stoplist = stopwords.words('english')
    stoplist += ['.', ',', '?', '-', '–', '«', '»', '(', ')', ':', ';', '#', '!', '$', '@', '%', '^', '*', '&', '*', '+', '']
    stemmer = SnowballStemmer('english')

    cleanWords = words[:]
    for token in words:
        if token in stoplist:
            cleanWords.remove(token)
    
    result = cleanWords[:]
    for index, value in enumerate(cleanWords):
        result[index] = stemmer.stem(value)
    
    return result

def l(p): # amortiguar
    return np.log10(1 + p)

def scoreCos(q, doc):
    return np.dot(q, doc) / (np.linalg.norm(q) * np.linalg.norm(doc))

def retrieval(collection, query, funcScore):
    result = []
    for i in range(len(collection)):
        sim = funcScore(query, collection[i])
        result.append( (i+1, sim) )   # [(doc1, sc1), (doc2, sc2), ...]
    result.sort(key = lambda tup: tup[1], reverse = True)
    return result

collection = [
    l(np.array([15,5,20,25])),
    l(np.array([30,0,22,0]))
]
query = l(np.array([115,10,2,0]))

result = retrieval(collection, query, scoreCos)
print("Score coseno: ", result, "\n")

query1 = parse("What city and country does Mario live in?")
print("Parsing query -> ", query1, "\n")

query2 = parse("Brazil Vaccine Scandal Imperils Bolsonaro as Protests Spread")
print("Parsing query -> ", query2, "\n")
