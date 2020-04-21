#!/usr/bin/python3
''' Start Flask. '''
from flask import Flask, abort, render_template

app = Flask(__name__, template_folder='./templates')
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


@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    ''' Return python page data. '''
    text = text.replace('_', ' ')
    return "Python " + text


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    ''' Return number page data. '''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    ''' Display HTML '''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    ''' Return number_odd_or_even page data '''
    return render_template('6-number_odd_or_even.html', n=n)
    abort(404)

if __name__ == '__main__':
    app.run()
