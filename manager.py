__author__ = 'SolPie'
from flask.ext.script import Manager

from pixtch.flaskPixtch import create_app
from pixtch.modules import db

app = create_app()

manager = Manager(app)


@manager.command
def hello():
    print "hello"


@manager.option('-n', '--name', help='Your name')
def hello2(name):
    print "hello", name


if __name__ == "__main__":
    manager.run()