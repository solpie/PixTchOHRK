# -*- coding:utf-8 -*-
__author__ = 'SolPie'
import os

from flask import Flask, render_template, request, g

application = app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = "yeah, not actually a secret"
# SECRET_KEY = "yeah, not actually a secret"
#
@app.route('/')
def welcome():
    return render_template('pixtch/index.html')


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
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('pixtch/postDetail.html', entries=entries)


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
    from admin.views import mod as admin

    # app.register_blueprint(admin)
    app.register_blueprint(admin, url_prefix='/admin')

    pass


from database import db_session


def init_database():
    from database import init_db
    init_db()


def init_admin():
    from admin.views import init
    init(app)
    # from flask.ext.admin import Admin
    # admin = Admin(app, name='Pixtch Backend')
    #
    # from flask.ext.admin.contrib.sqlamodel import ModelView
    # from auth.models import User
    # admin.add_view(ModelView(User, db_session))
    # #
    # from kn.models import KnPost, KnCategory, Tag
    # admin.add_view(ModelView(Tag, db_session))

    # admin.add_view(ModelView(name='Hello 1', endpoint='KnPost', category='坑'))

    #
    # from flask.ext.admin.contrib.fileadmin import FileAdmin
    #
    # path = os.path.join(os.path.dirname(__file__), 'static')
    # admin.add_view(FileAdmin(path, '/static/', name='Static Files'))
    #


def init_Path():
    import sys

    sys.path.insert(0, 'libs')
    print app.config.root_path


if __name__ == '__main__':
    init_Path()
    init_database()
    init_bluePrint()
    init_admin()
    # from test import bp
    # app.register_blueprint(bp)
    print 'init_end'
    # print app.url_rule_class.alias
    #
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)

