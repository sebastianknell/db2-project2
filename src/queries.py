import math
import buildIndex
from nltk import SnowballStemmer, word_tokenize
from nltk.corpus import stopwords

N = 53292

def getIDF(terms):
    df = len(terms)
    return math.log10(N/df)

def getTF_IDF(tf,idf):
    tf_idf_vec = []
    for j in tf:
        i = j[1]
        tf_idf_vec.append((j[0], i * idf))
    return tf_idf_vec

def getLogFreq(tf):
    logFreq_vec = []
    for j in tf:
        i = j[1]
        if( i > 0):
            logFreq_vec.append((j[0], 1 + math.log10(i)))
        else:
            logFreq_vec.append((j[0], 0))
    return logFreq_vec

def getNorm(terms):
    norm = 0
    for term in terms:
        tf = term[1]
        norm += (tf**2)
    return math.sqrt(norm)

def getNormalizedTerms(terms, norm):
    normalized = []
    for term in terms:
        tf = term[1]
        normalized.append((term[0], tf/norm))
    return normalized

def getCosineSim(normTerms1, normTerms2):
    sum = 0
    for j in range(len(normTerms1)):
        sum += normTerms1[j][1]*normTerms2[j][1]
    return sum

def getScore(vec):
    vec = getLogFreq(vec)
    idf = getIDF(vec)
    vec = getTF_IDF(vec, idf)
    norm_vec = getNormalizedTerms(vec, getNorm(vec))
    return norm_vec

def parse(query):
    words = word_tokenize(query.lower())
    stoplist = stopwords.words('english')
    stoplist += ['.', ',', '?', '-', '–', '«', '»', '(', ')', ':', ';', '#', '!', '$', '@', '%', '^', '', '&', '', '+', '']
    stemmer = SnowballStemmer('english')

    cleanWords = words[:]
    for token in words:
        if token in stoplist:
            cleanWords.remove(token)

    result = cleanWords[:]
    for index, value in enumerate(cleanWords):
        result[index] = stemmer.stem(value)

    return result

# norm_tfidf1 = getNormalizedTerms(tf_idf1, getNorm(tf_idf1))
# norm_tfidf2 = getNormalizedTerms(tf_idf2, getNorm(tf_idf2))
# print("Normalized TF-IDF Cosime sim: ")
# print(getCosSim(norm_tfidf1, norm_tfidf2))

# index = buildIndex.readIndex("src/data/index.txt")
query = "The election of Donald Trump and running mate Mike Pence set off panic in gay, lesbian, bisexual and transgender communities across the country"
parsed = parse(query)

qf = {}
for term in parsed:
    if term in qf.keys():
        qf[term] += 1
    else:
        qf[term] = 1

for term in parsed:
    q_tfidf = list(qf.items())
    qScore = getScore(q_tfidf)

print(qScore)

# scores = {}
# for term in parsed:
#     postingList = list(index[term].items())
#     vec = getScore(postingList)
#     for pair in vec:
#         if pair[0] in scores.keys():
#             scores[pair[0]] += pair[1] * qf[term]
#         else:
#             scores[pair[0]] = pair[1] * qf[term]
# docLen = buildIndex.readDocNorms()
# for d in scores.keys():
#     scores[d] = scores[d]/docLen[d]
# scores = {key:val for key,val in sorted(scores.items(), key = lambda elem: elem[1], reverse=True)}

# print(list(scores.items())[:10])

# ss = [('afecto',115), ('celoso', 10), ('chisme', 2), ('borrascoso', 0)]
# op = [('afecto',58), ('celoso', 7), ('chisme', 0), ('borrascoso', 0)]
# cb = [('afecto',20), ('celoso', 11), ('chisme', 6), ('borrascoso', 38)]
# q = [('afecto', 1), ('celoso', 10),('chisme',5), ('borrascoso', 1)]
# scoreSS = getScore(ss)
# scoreOP = getScore(op)
# scoreCB = getScore(cb)
# scoreQ = getScore(q)
# print(scoreSS)
# print(scoreOP)
# print(scoreCB)
# print(scoreQ)
# print('\n')
# print(getCosineSim(scoreQ, scoreSS))
# print(getCosineSim(scoreQ, scoreOP))
# print(getCosineSim(scoreQ, scoreCB))