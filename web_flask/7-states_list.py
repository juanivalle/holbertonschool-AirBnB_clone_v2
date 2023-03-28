#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/states_list', strict_slash=False)
def states_list():
    """List all states"""
    from models import storage
    from models.state import State
    
    states = storage.all(State)
    list = []
    for val in states.values():
        list.append(val)
    
    return render_template('7-states_list.html', states_list=list)

@app.teardown_appcontext
def close_state():
    from models import storage
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)