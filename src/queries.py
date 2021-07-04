import math
import buildIndex

N = 154398

def getFrequency(term):
    result = []
    for key in term:
        result.append(term[key])
    return result

def getFrequencies(dict):
    queryTfs = {}
    for term in dict:
        queryTfs[term] = getFrequency(result[term])
    return queryTfs

def getDocIDS(dict):
    return dict.keys()

def getDocFrequency(frequencies):
    return len(frequencies)

def getIDF(df, n):
    return math.log10(n/df)

def getTF_IDF(tf,idf):
    tf_idf_vec = []
    for i in tf:
        tf_idf_vec.append(i * idf)
    return tf_idf_vec

def getLogFreq(tf):
    logFreq_vec = []
    for i in tf:
        if( i > 0):
            logFreq_vec.append(1 + math.log10(i))
        else:
            logFreq_vec.append(0)
    return logFreq_vec

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
#print(getCosSim(norm_ss, norm_op))

#index = buildIndex.readIndex(buildIndex.INDEX_FILE)
#print(index['•'])
#print(index['†††'])  -> {28910: 1}
term1 = {28910: 1}
term2 = {13: 3, 26: 23, 40: 15, 117: 11, 155: 22, 163: 5, 213: 23, 214: 13, 215: 3, 251: 12, 281: 22, 304: 12, 368: 4, 397: 24, 483: 10, 507: 8, 532: 26, 552: 28, 553: 11, 650: 5, 705: 22, 728: 22, 754: 24, 811: 12, 894: 23, 922: 24, 923: 18, 945: 24, 946: 15, 984: 3, 1028: 21, 1063: 21, 1085: 24, 1118: 16, 1123: 9, 1125: 13, 1155: 5, 1157: 3, 1168: 22, 1193: 11, 1199: 15, 1281: 24, 1290: 2, 1292: 14, 1299: 23, 1303: 26, 1326: 18, 1331: 9, 1345: 14, 1393: 5, 1434: 11, 1459: 24, 1480: 25, 1549: 23, 1574: 21, 1576: 17, 1596: 25, 1623: 22, 1651: 24, 1652: 12, 1758: 20, 1773: 21, 1803: 12, 1805: 6, 1948: 10, 1959: 9, 1984: 11, 2014: 11, 2023: 14, 2107: 13, 2143: 27, 2144: 13, 2149: 10, 2170: 16, 2208: 3, 2227: 24, 2290: 24, 2299: 13, 2322: 23, 2386: 11, 2419: 18, 2451: 24, 2453: 3, 2477: 10, 2494: 23, 2542: 2, 2558: 21, 2571: 7, 2877: 4, 2878: 4, 2912: 15, 2943: 23, 2957: 16, 3049: 17, 3061: 3, 3121: 14, 3129: 13, 3154: 13, 3226: 3, 3300: 5, 3305: 9, 3318: 7, 3394: 10, 3431: 29, 3433: 3, 3481: 5, 3487: 4, 3569: 6, 3662: 13, 3666: 7, 3667: 7, 3719: 7, 3798: 14, 3904: 10, 3950: 15, 4076: 12, 4091: 12, 4144: 10, 4165: 10, 4195: 14, 4205: 15, 4232: 1, 4262: 6, 4274: 23, 4363: 18, 4400: 23, 4418: 3, 4426: 14, 4457: 21, 4458: 21, 4462: 5, 4469: 13, 4474: 22, 4475: 17, 4492: 8, 4501: 3, 4546: 20, 4556: 4, 4560: 17, 4575: 22, 4576: 11, 4599: 15, 4636: 23, 4649: 23, 4666: 20, 4682: 13, 4736: 25, 4737: 13, 4772: 26, 4773: 10, 4787: 24, 4800: 12, 4873: 13, 4891: 7, 4900: 10, 4925: 21, 4935: 21, 4953: 22, 4972: 23, 5060: 23, 5076: 20, 5125: 23, 5206: 20, 5239: 7, 5247: 16, 5330: 4, 5386: 3, 5438: 5, 5449: 3, 5459: 7, 5473: 8, 5491: 11, 5631: 3, 5639: 15, 5674: 4, 5848: 20, 5857: 3, 5871: 3, 5891: 10, 5902: 9, 5909: 10, 5956: 5, 5964: 10, 5976: 11, 5978: 8, 6023: 4, 6037: 8, 6052: 19, 6122: 22, 6153: 13, 6162: 10, 6178: 3, 6197: 3, 6212: 42, 6217: 12, 6279: 23, 6292: 23, 6356: 23, 6364: 23, 6366: 8, 6406: 27, 6411: 18, 6421: 11, 6433: 19, 6441: 24, 6506: 11, 6666: 11, 6682: 18, 6706: 10, 6722: 10, 6956: 18, 7085: 23, 7091: 23, 7168: 24, 7289: 9, 7353: 11, 7418: 19, 7420: 3, 7424: 11, 7426: 3, 7427: 21, 7430: 4, 7442: 19, 7491: 3, 7506: 7, 7509: 24, 7579: 13, 7634: 9, 7652: 21, 7667: 11, 7680: 20, 7700: 6, 7743: 13, 7748: 19, 7770: 21, 8061: 1, 8492: 1, 8627: 1, 8865: 5, 9386: 4, 9649: 3, 9662: 2, 9784: 1, 9961: 1, 10087: 3, 10180: 1, 10241: 2, 10265: 2, 10645: 3, 11345: 1, 12290: 1, 12353: 1, 12399: 2, 12650: 1, 13457: 1, 13670: 1, 14004: 1, 14222: 1, 14776: 1, 15392: 1, 16838: 1, 17037: 1, 17533: 1, 17721: 2, 18999: 1, 19357: 1, 19407: 4, 19623: 5, 19709: 2, 21024: 1, 21309: 1, 21388: 1, 21792: 1, 21886: 1, 22232: 3, 22293: 1, 22621: 1, 22652: 2, 23262: 1, 23679: 1, 24137: 1, 24446: 1, 24508: 3, 25088: 5, 25229: 4, 26168: 1, 26216: 1, 26408: 2, 26419: 10, 26436: 1, 26929: 1, 27225: 1, 28396: 2, 28739: 2, 28753: 1, 28995: 2, 29120: 1, 29904: 1, 30026: 1, 30621: 1, 30643: 1, 30832: 1, 31227: 4, 31235: 2, 31326: 4, 31654: 3, 31826: 8, 32248: 5, 32257: 5, 32259: 4, 32298: 5, 32731: 12, 32924: 9, 33623: 4, 33968: 5, 33975: 7, 34049: 3, 34208: 4, 34283: 3, 34385: 3, 34782: 3, 35156: 6, 35962: 9, 36067: 3, 36273: 3, 36277: 18, 36448: 4, 36473: 3, 36492: 4, 36563: 11, 36717: 3, 36779: 3, 36860: 22, 36880: 3, 36908: 6, 36924: 6, 37165: 17, 37419: 13, 37571: 1, 37662: 4, 37672: 3, 38212: 4, 38240: 13, 38253: 4, 38368: 5, 38387: 4, 38492: 5, 39141: 3, 39412: 3, 39481: 3, 39515: 6, 39569: 6, 39637: 4, 39717: 28, 39718: 5, 39734: 3, 39825: 7, 39896: 6, 39975: 16, 39997: 5, 40000: 4, 40201: 3, 40375: 13, 40430: 6, 40733: 5, 40885: 3, 40913: 2, 40994: 3, 41036: 6, 41080: 6, 41236: 5, 41390: 6, 41487: 2, 41496: 6, 41630: 5, 41705: 3, 41737: 5, 41892: 7, 42421: 4, 42444: 8, 42451: 9, 42456: 3, 42556: 3, 43109: 3, 44740: 1, 45123: 8, 45200: 5, 47612: 3, 48572: 10, 48689: 29, 49710: 1}

term3 = {10: 3, 15: 5, 16: 10, 20: 2}
term4 = {9: 8, 15: 2, 14: 2, 20: 13}

# tf1 = getFrequency(term3)
# tf2 = getFrequency(term4)

# tf1 = getLogFreq(term3)
# tf2 = getLogFreq(term4)

# df1 = getDocFrequency(term3)
# df2 = getDocFrequency(term4)

# idf1 = getIDF(df1, N)
# idf2 = getIDF(df2, N)

# tf_idf1 = getTF_IDF(tf1, idf1)
# tf_idf2 = getTF_IDF(tf2, idf2)

# print(tf_idf1)
# print(tf_idf2)


# norm_t3 = getNormalizedTerms(term3, getNorm(term3))
# norm_t4 = getNormalizedTerms(term4, getNorm(term4))
# print("Normalized Terms Cosine sim: ")
# print(getCosSim(norm_t3, norm_t4))

# norm_tfidf1 = getNormalizedTerms(tf_idf1, getNorm(tf_idf1))
# norm_tfidf2 = getNormalizedTerms(tf_idf2, getNorm(tf_idf2))
# print("Normalized TF-IDF Cosime sim: ")
# print(getCosSim(norm_tfidf1, norm_tfidf2))

index = buildIndex.readIndex("src/data/test.txt")
query = ['+107', '+11', '+16']



result = {}
for term in query:
    for i in index:
        if(i == term):
            result[term] = index[i]

queryTfs = getFrequencies(result)
print(queryTfs)
print(getDocIDS(result))