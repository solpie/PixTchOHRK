# -*- coding:utf-8 -*-
__author__ = 'SolPie'
import os

from flask import Flask, render_template

application = app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'interesting'


@app.before_request
def before_request():
    # g.db = connect_db()
    pass


from database import db_session


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
    # print __name__, '>>shutdown_session'
    pass


@app.route('/env')
def env():
    return os.environ.get("VCAP_SERVICES", "{}")


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
    from home.views import route_home
    from auth.views import route_auth
    from kn.views import route_kn
    from admin.views import route_admin as admin

    app.register_blueprint(route_home)
    app.register_blueprint(route_auth)
    app.register_blueprint(route_kn, url_prefix='/kn')
    app.register_blueprint(admin)
    pass


def init_database():
    from database import init_db

    init_db()


def init_ext():
    from admin.views import init_admin
    from auth.views import init_auth
    from flask.ext.bootstrap import Bootstrap

    init_auth(app)
    init_admin(app)
    Bootstrap(app)


def init_Path():
    import sys

    sys.path.insert(0, 'libs')
    print __name__, app.config.root_path


if __name__ == '__main__':
    init_Path()
    # init_database()
    init_bluePrint()
    init_ext()
    import datetime

    t = datetime.datetime.now()
    print __name__, '>>init..ok', t
    # print app.url_rule_class.alias
    #
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)

