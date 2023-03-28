#!/usr/bin/python3
"""comments"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/cities_by_states', strict_slash=False)
def cities_by_states():
    """comments"""
    
    from models import storage
    from models.state import State
    
    states_dict = storage.all(State)
    
    dict = {}
    for val in states_dict.values():
        dict[val] = State.cities
    
    return render_template('8-cities_by_states.html', dict=dict)

@app.teardown_appcontext
def close(exception):
    """Close database connection"""
    
    from models import storage
    
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
