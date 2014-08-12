import os
import sqlite3
import json
from flask import Flask, g, make_response, render_template

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'wanted.db'),
    DEBUG=True,
))
app.config.from_envvar('WANTED_SETTINGS', silent=True)

def connect_db():
    """Connects to the database"""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database agian at the end of a request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/wanteddata')
def get_entries():
    db = get_db()
    print("getting data")
    cursor = db.execute('select * from wanted')
    entries = [dict(zip([column[0] for column in cursor.description], row)) 
                for row in cursor.fetchall()]
    all_data = json.dumps(entries)
    return all_data

@app.route('/')
def home():
    #return make_response(open('index.html').read())
    return render_template('index.html')
    #return "hello"

if __name__ == '__main__':
    app.run()
