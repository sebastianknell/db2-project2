import math
import buildIndex
from nltk import SnowballStemmer, word_tokenize
from nltk.corpus import stopwords


N = 154398

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
            logFreq_vec.append((j[0], 1 + math.log(i)))
        else:
            logFreq_vec.append((j[0], 0))
    return logFreq_vec

def getNorm(terms):
    norm = 0
    for tf in terms:
        norm += (tf**2)
    return math.sqrt(norm)

def getNormalizedTerms(terms, norm):
    normalized = []
    for tf in terms:
        normalized.append(tf/norm)
    return normalized

def getCosSim(normTerms1, normTerms2):
    cos = sum([normTerms1[i]*normTerms2[i] for i in range(len(normTerms1))])
    return cos

def getScore(vec):
    vec = getLogFreq(vec)
    idf = getIDF(vec)
    vec = getTF_IDF(vec, idf)
    return vec

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

index = buildIndex.readIndex("src/data/index.txt")
query = "The election of Donald Trump and running mate Mike Pence set off panic in gay, lesbian, bisexual and transgender communities across the country"
parsed = parse(query)



qf = {}
for term in parsed:
    if term in qf.keys():
        qf[term] += 1
    else:
        qf[term] = 1


scores = {}
for term in parsed:
    postingList = list(index[term].items())
    vec = getScore(postingList)
    for pair in vec:
        if pair[0] in scores.keys():
            scores[pair[0]] += pair[1] * qf[term]
        else:
            scores[pair[0]] = pair[1] * qf[term]
docLen = buildIndex.readDocNorms()
for d in scores.keys():
    scores[d] = scores[d]/docLen[d]
scores = {key:val for key,val in sorted(scores.items(), key = lambda elem: elem[1], reverse=True)}

print(list(scores.items())[:10])