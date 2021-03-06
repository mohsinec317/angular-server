import flask
from flask import request, jsonify, make_response
import json
from flask_cors import CORS


app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/json', methods=['GET'])
def loaddata():
    id = request.query_string
    with open(id) as f:
        data = json.load(f)
    return make_response(jsonify(data))

app.run()
