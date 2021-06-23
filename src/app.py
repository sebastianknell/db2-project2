from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route('/search/<query>', methods=['GET'])
def search(query):
    print("Processing query")
    print(query)
    return "Query processed"