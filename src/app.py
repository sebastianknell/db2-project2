from flask import Flask, Response
from flask import request
from flask_cors import CORS
import pandas as pd
import json
import time

import index as idx
import queries
from entities import New

app = Flask(__name__)
cors = CORS(app)

data = pd.read_csv(idx.DATA_FILE, encoding='UTF-8')
termIndex = idx.readIndex(idx.TERM_INDEX_FILE)
docNorms = idx.readDocNorms()


def getNews(query):
    docIDS = queries.processQuery(query, termIndex, docNorms)
    news = []
    for id in docIDS:
        doc = data.iloc[id]
        anew = New(id, doc['title'], doc['publication'], doc['year'], doc['content'])
        news.append(vars(anew))
    return news


@app.route("/")
def index():
    return "<p>Aqui no hay nada</p>"


@app.route('/search', methods=['POST'])
def search():
    msg = json.loads(request.data)
    query = msg['query']
    print("Query {} recieved".format(query))
    news = getNews(query)
    s = json.dumps(news)
    return Response(s, 200, mimetype='application/json')
