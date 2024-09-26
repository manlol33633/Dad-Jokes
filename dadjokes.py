import flask
from flask import request
import json
import random

app = flask.Flask(__name__)

with open ('dadjokes.json') as jokes_json:
    dad_jokes = json.load(jokes_json)

@app.route('/', methods=['GET'])
def home():
    return {'success': True, 'message': 'This is the home page'}

@app.route('/random')
def index():
    return dad_jokes[random.randint(0, len(dad_jokes) - 1)]['joke']

@app.route('/joke')
def joke():
    joke_id = request.args.get("id")
    for joke in dad_jokes:
        if (joke['id'] == joke_id):
            return joke['joke']
    return 'Joke not found'

app.run(host='127.0.0.1', port=3001)
