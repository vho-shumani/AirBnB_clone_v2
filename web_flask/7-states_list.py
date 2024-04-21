from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown.appcontext
def teardown():
    """remove the current SQLAlchemy Session"""
    storage.close()
    

@app.route('/states_list', strict_slashes=False)
def states():
    """Display a HTML page with a list of all State objects."""
    sorted_states = storage.all('State').value()
    sorted_states = sorted(states, key=lambda x: x.name)
    
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')