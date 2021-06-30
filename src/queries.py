import math

# Test structures
articles = []
example1 = dict({'article':1250,'tf':1})
example2 = dict({'article':10780,'tf':2})
example3 = dict({'article':33333,'tf':3})
articles.append(example1)
articles.append(example2)
articles.append(example3)

def getFrequency(term):
    return term['tf']

def getDocFrequency(dictionary):
    return len(dictionary)

def getIDF(df, n):
    return math.log10(n/df)

def getTF_IDF(tf,idf):
    return tf*idf

def getLogFreq(tf):
    if(tf > 0):
        return 1+math.log10(tf)
    else:
        return 0

def getNorm(terms):
    norm = 0
    for tf in terms:
        norm += (tf**2)
    return math.sqrt(norm)

#Test Term Frequencies
ss = [3.06, 2.00, 1.30, 0]
op = [2.76, 1.85, 0, 0]

def getNormalizedTerms(terms, norm):
    normalized = []
    for tf in terms:
        normalized.append(tf/norm)
    return normalized

#Test normalized term frequencies
norm_ss = getNormalizedTerms(ss , getNorm(ss))
norm_op = getNormalizedTerms(op , getNorm(op))

def getCosSim(normTerms1, normTerms2):
    cos = sum([normTerms1[i]*normTerms2[i] for i in range(len(normTerms1))])
    return cos

#Test cosine sim between ss and op
print(getCosSim(norm_ss, norm_op))