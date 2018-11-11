# Ricky Galliani

from src.message import Message, EncodedMessage

from flask import jsonify, request

import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Enbase</h1>"


@app.route('/encode', methods=['GET'])
def encode():
    if 'text' in request.args:
        text = request.args['text']
    else:
        return '[ERROR]: Please provide text to encode.'
    encoding = Message(text).encode()
    return jsonify({'text': encoding.text, 'key': encoding.key})


@app.route('/decode', methods=['GET'])
def decode():
    if 'text' in request.args and 'key' in request.args:
        text = request.args['text']
        key = int(request.args['key'])
    else:
        return '[Error]: Please provide text to decode along with key.'
    original_text = EncodedMessage(text, key).decode().text
    print("original_text = {}".format(original_text))
    return jsonify({'text': original_text})

app.run()
