__author__ = 'SolPie'
import time
import sys
import os
import json
from flask import Flask, Request, Response, url_for,render_template


application = app = Flask('wsgi')
#admin
# from pixtch.admin import Admin
from flask.ext.admin import Admin
#
@app.route('/')
def welcome():
    return render_template('home.html')


@app.route('/static')
def static():
    return url_for('static')


@app.route('/uppo/<upponame>')
def show_uppo_profile(upponame):
    return 'uppo %s' % upponame


@app.route('/kn/<int:kid>')
def show_kn_post(kid):
    return 'keng %d' % kid


@app.route('/env')
def env():
    return os.environ.get("VCAP_SERVICES", "{}")


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


if __name__ == '__main__':
    # module
    Admin(app)
    #
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)

