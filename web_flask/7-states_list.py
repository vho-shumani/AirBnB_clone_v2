#!/usr/bin/python3
"""Starts a flask web application"""


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()
    

@app.route('/states_list', strict_slashes=False)
def states():
    """Display a HTML page with a list of all State objects."""
    sorted_states = sorted(storage.all(State).values(), key=lambda x: x.name)
    
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')