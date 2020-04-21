#!/usr/bin/python3
''' Start Flask. '''
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    ''' Return page. '''
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    ''' Return page. '''
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    ''' Return c page data. '''
    text = text.replace('_', ' ')
    return "C " + text

if __name__ == '__main__':
    app.run()