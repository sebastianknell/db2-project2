from flask import Flask, Response
from flask import request
from flask_cors import CORS
import json
import time

from entities import New

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"


@app.route('/search', methods=['POST'])
def search():
    msg = json.loads(request.data)
    print("Query {} recieved".format(msg['query']))
    new1 = New(1, 'Some title', 'New York Times', 2021, 'Some content')
    new2 = New(2, 'Some title', 'New York Times', 2021, 'Some content')
    l = [vars(new1), vars(new2)]
    time.sleep(2)
    s = json.dumps(l)
    return Response(s, 200, mimetype='application/json')
