#!/usr/bin/python3
''' Start a Flask '''
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__, template_folder='./templates')
app.url_map.strict_slashes = False


@app.route('/states_list', strict_slashes=False)
def states_list():
    ''' Display HTML  '''
    return render_template('7-states_list.html',
                           states=storage.all(State).values())


@app.teardown_appcontext
def remove_session(response_or_exc):
    ''' Close SQLAlchemy session '''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)