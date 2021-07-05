import math
import index as idx
import pandas as pd
from tokenizer import parse

N = 53292


def getIDF(terms):
    df = len(terms)
    return math.log10(N/df)


def getTF_IDF(tf, idf):
    tf_idf_vec = []
    for j in tf:
        i = j[1]
        tf_idf_vec.append((j[0], i * idf))
    return tf_idf_vec


def getLogFreq(tf):
    logFreq_vec = []
    for j in tf:
        i = j[1]
        if(i > 0):
            logFreq_vec.append((j[0], 1 + math.log10(i)))
        else:
            logFreq_vec.append((j[0], 0))
    return logFreq_vec


def getNorm(terms):
    norm = 0
    for tf in terms:
        norm += (tf**2)
    return math.sqrt(norm)


def normalizeTerms(terms, norm):
    normalized = []
    for tf in terms.items():
        normalized.append((tf[0], tf[1]/norm))
    return normalized


def getCosSim(normTerms1, normTerms2):
    cos = sum([normTerms1[i]*normTerms2[i] for i in range(len(normTerms1))])
    return cos


def getScore(vec):
    vec = getLogFreq(vec)
    idf = getIDF(vec)
    vec = getTF_IDF(vec, idf)
    return vec


def getTermFrequenies(terms):
    tf = {}
    for term in terms:
        if term in tf.keys():
            tf[term] += 1
        else:
            tf[term] = 1
    return tf


def processQuery(query, termIndex, docNorms):
    parsed = parse(query)
    wtq = getTermFrequenies(parsed)

    scores = {}
    for term in parsed:
        plist = termIndex.get(term)
        idf = 0 if plist == None else getIDF(plist)
        wtq[term] = wtq[term] * idf

        # tf only. TODO change
        if plist != None:
            for doc, tf in plist.items():
                if doc in scores.keys():
                    scores[doc] += tf * wtq[term]
                else:
                    scores[doc] = tf * wtq[term]

    for d in scores.keys():
        scores[d] = scores[d]/docNorms[d]

    scores = {key: val for key, val in sorted(
        scores.items(), key=lambda elem: elem[1], reverse=True)}

    return [int(item[0]) for item in list(scores.items())[:10]]
