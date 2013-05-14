__author__ = 'SolPie'
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os

from bae.core.const import *

user, pw, host, port, db = MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, 'MVwslEoiYLtUAerKTSuE'

engine = create_engine('mysql://' + user + ':' + pw + '@' + host + ':' + port + '/' + db, convert_unicode=True,
                       echo=False)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

basedir = os.path.abspath(os.path.dirname(__file__))


def session_add(base):
    db_session.add(base)


def session_commit():
    db_session.commit()


def connect(user, pw, host, port, db):
    # engine = create_engine('mysql://' + user + ':' + pw + '@' + host + ':' + port + '/' + db, convert_unicode=True,
    #                        echo=False)
    # db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    # Base.query = db_session.query_property()
    # create_db(engine)
    pass


def create_db(e):
    import kn.models
    import auth.models
    import uppo.models

    Base.metadata.create_all(bind=e)
    print __name__, '>>create db'


def get_base_metadata():
    from kn.models import *
    from auth.models import *
    from uppo.models import *

    return Base.metadata


def autogenerate():
    'alembic revision --autogenerate -m "Added account table"'
    pass


def upgrade():
    'alembic upgrade head'
    pass


if __name__ == '__main__':
    create_db()
