# -*- coding:utf-8 -*-
__author__ = 'SolPie'
import os

from flask import Flask, render_template, g
from const import *

application = app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'interesting'

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/test.db'


@app.before_request
def before_request():
    if app.config[ENV_BAE]:
        g.db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASS,
                               MYSQL_DB, port=int(MYSQL_PORT))
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
    return render_template('404.html', e=error)


@app.errorhandler(401)
def error401(error):
    return render_template('401.html', e=error)


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
    from flask.ext.sqlalchemy import SQLAlchemy

    from database import init_db

    init_db()


def init_ext():
    from admin.views import init_admin
    from auth.views import init_auth
    from flask.ext.bootstrap import Bootstrap

    # import flask_sijax

    init_auth(app)
    init_admin(app)
    Bootstrap(app)
    #####################bae#############################
    bae = app.config[ENV_BAE] = False
    if bae:
        from bae.core.wsgi import WSGIApplication

        application = WSGIApplication(app)
        from sae.const import (MYSQL_HOST, MYSQL_HOST_S,
                               MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB)
        ########################################################

    sae = app.config['SAE_RUN'] = False
    if sae:
        from sae.const import (MYSQL_HOST, MYSQL_HOST_S,
                               MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB
                               )

        # app.config['SIJAX_STATIC_PATH'] = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
        # app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
        # flask_sijax.Sijax(app)


def init_Path():
    import sys

    sys.path.insert(0, 'libs')
    print __name__, app.config.root_path


def main():
    init_Path()
    # init_database()
    init_bluePrint()
    init_ext()


if __name__ == '__main__':
    main()

    import datetime

    t = datetime.datetime.now()
    print __name__, '>>init..ok', t
    # print app.url_rule_class.alias
    #
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)

