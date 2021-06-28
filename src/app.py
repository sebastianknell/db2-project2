from flask import Flask, Response
from flask import request
from flask_cors import CORS
import json

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
    new = New(1, 'Some title', 'New York Times', 2021, 'Some content')
    s = json.dumps(vars(new))
    return Response(s, 200, mimetype='application/json')
