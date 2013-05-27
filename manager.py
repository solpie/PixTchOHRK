__author__ = 'SolPie'
import sys
import os

sys.path.insert(0, os.path.join('.', 'pixtch'))
from flask.ext.script import Manager

from flaskPixtch import create_app
from modules import db
from auth.models import User
from kn.models import KnPost

app = create_app()

manager = Manager(app)
app.setup()


@manager.command
def hello():
    print "hello"


@manager.command
def init():
    db.init_app(app)
    db.drop_all(app=app)
    db.create_all(app=app)
    print "init...db"
    email = app.config.get('ADMINS')[0]
    admin = User('admin', email, '-+')
    db.session.add(admin)
    db.session.commit()
    print "create...admin"


@manager.command
def post():
    db.init_app(app)
    for i in range(0, 10):
        p = KnPost(u'test post ' + str(i))
        p.html_content = 'this is a test post from manager'
        db.session.add(p)
    db.session.commit()
    print 'create test post'


@manager.command
def clone():
    db.session
    src_uri = ''
    print 'clone db from', src_uri


if __name__ == "__main__":
    manager.run()