# Ricky Galliani

from src.message import Message, EncodedMessage

from flask import jsonify, render_template, request

import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET', 'POST'])
def home():
    errors = []
    results = {}

    if request.method == 'POST':
        try:
            if 'text-to-encode' in request.form:
                encoding = Message(request.form['text-to-encode']).encode()
                results.update({
                    'encoded-text': encoding.text,
                    'key': encoding.key
                })
        except:
            errors.append("[ERROR]: Could not encode text.")

        try:
            if ('text-to-decode' in request.form) and \
               ('decode-key' in request.form):
                results.update({
                    'decoded-text': EncodedMessage(
                        request.form['text-to-decode'],
                        int(request.form['decode-key'])
                    ).decode().text
                })
        except: 
            errors.append("[ERROR]: Could not decode text.")

    return render_template('index.html', errors=errors, results=results)


if __name__ == '__main__':
    app.run()
