__author__ = 'SolPie'
import time
import sys
import os
import json
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, Request, Response, url_for, render_template, request, session, flash, redirect, g, abort


application = app = Flask(__name__)

#admin
# from pixtch.admin import Admin
from flask.ext.admin import Admin
#
@app.route('/')
def welcome():
    return render_template('pixtch/home.html')

# @app.route('/static')
# def static():
#     return url_for('static')
#
#
# @app.route('/static/css')
# def static_css():
#     return url_for('static_css')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('static/upload/upload.txt')


@app.route('/uppo/<upponame>')
def show_uppo_profile(upponame):
    return 'uppo %s' % upponame


@app.route('/kn/<int:kid>')
def show_kn_post(kid):
    return 'keng %d' % kid


@app.route('/env')
def env():
    return os.environ.get("VCAP_SERVICES", "{}")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('pixtch/login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


@app.route('/show')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('pixtch/postDetail.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)', [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


'''
database
'''
from contextlib import closing
# configuration
DATABASE = 'db/flaskr.db'
DEBUG = True
SECRET_KEY = 'dev key'
USERNAME = 'admin'
PASSWORD = '-+'
app.config.from_object(__name__)
app.config.from_envvar('APP_SETTINGS', silent=True)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('db/schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(e):
    g.db.close()


@app.route('/mongo')
def mongotest():
    from pymongo import Connection

    uri = mongodb_uri()
    conn = Connection(uri)
    coll = conn.db['ts']
    coll.insert(dict(now=int(time.time())))
    last_few = [str(x['now']) for x in coll.find(sort=[("_id", -1)], limit=10)]
    body = "\n".join(last_few)
    return Response(body, content_type="text/plain;charset=UTF-8")


def mongodb_uri():
    local = os.environ.get("MONGODB", None)
    if local:
        return local
    services = json.loads(os.environ.get("VCAP_SERVICES", "{}"))
    if services:
        creds = services['mongodb-1.8'][0]['credentials']
        uri = "mongodb://%s:%s@%s:%d/%s" % (
            creds['username'],
            creds['password'],
            creds['hostname'],
            creds['port'],
            creds['db'])
        print >> sys.stderr, uri
        return uri
    else:
        raise Exception, "No services configured"
'''
error
'''

@app.errorhandler(404)
def error404(error):
    return render_template('404.html')


if __name__ == '__main__':
    # module
    Admin(app)
    init_db()
    print os.path.abspath('')

    #
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='127.0.0.1', port=port)

