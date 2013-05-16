__author__ = 'SolPie'
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('mysql+pymysql://root:-+@127.0.0.1/test', convert_unicode=True, echo=False)

# engine = create_engine('sqlite:///db/test.db', convert_unicode=True, echo=False)

#################################################
import os

if 'SERVER_SOFTWARE' in os.environ:
    uri = os.environ.get('MYSQL')
    print "This is online environ"
else:
    uri = 'sqlite:///db/test.db'
    print "This is local environ"
##################################################
engine = create_engine(uri, convert_unicode=True, echo=False)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def session_add(base):
    db_session.add(base)


def session_commit():
    db_session.commit()


def create_db():
    import kn.models
    import auth.models
    import uppo.models

    create_all(bind=engine)
    print __name__, '>>create db'


def create_all(bind=None, table=None, checkfirst=True):
    Base.metadata.create_all(bind, table, checkfirst)


def drop_all(bind=None, table=None, checkfirst=True):
    Base.metadata.drop_all(bind, table, checkfirst)


def get_base_metadata():
    from kn.models import *
    from auth.models import *
    from uppo.models import *

    return Base.metadata

#####################new##################
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


######################
def autogenerate():
    'alembic revision --autogenerate -m "Added account table"'
    pass


def upgrade():
    'alembic upgrade head'
    pass


if __name__ == '__main__':
    create_db()
