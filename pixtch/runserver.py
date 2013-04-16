# -*- coding:utf-8 -*-
__author__ = 'SolPie'
import os

from flask import Flask, render_template, request
from flask.ext import login

application = app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = "yeah, not actually a secret"
# SECRET_KEY = "yeah, not actually a secret"
#
@app.route('/')
def index():
    return render_template('pixtch/index.html', uppo=login.current_user)


@app.before_request
def before_request():
    # g.db = connect_db()
    pass


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
    pass


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('static/upload/upload.txt')


@app.route('/uppo/<upponame>')
def show_uppo_profile(upponame):
    return 'uppo %s' % upponame


@app.route('/env')
def env():
    return os.environ.get("VCAP_SERVICES", "{}")


@app.route('/show')
def show_entries():
    return 'show'
    # return redirect(url_for('index'))


'''
error
'''


@app.errorhandler(404)
def error404(error):
    return render_template('404.html')


'''
init
'''


def init_bluePrint():
    from auth.views import route_auth

    app.register_blueprint(route_auth)
    from kn.views import route_kn

    app.register_blueprint(route_kn, url_prefix='/kn')
    from admin.views import route_admin as admin

    app.register_blueprint(admin)

    pass


from database import db_session


def init_database():
    from database import init_db

    init_db()


def init_ext():
    from admin.views import init_admin

    init_admin(app)
    from auth.views import init_auth

    init_auth(app)


def init_Path():
    import sys

    sys.path.insert(0, 'libs')
    print app.config.root_path


if __name__ == '__main__':
    init_Path()
    init_database()
    init_bluePrint()
    init_ext()
    # from test import bp
    # app.register_blueprint(bp)
    print __name__, '>>init_end'
    # print app.url_rule_class.alias
    #
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)

