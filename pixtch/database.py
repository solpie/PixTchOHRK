__author__ = 'SolPie'
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os

engine = create_engine('sqlite:///db/test.db', convert_unicode=True, echo=False)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

basedir = os.path.abspath(os.path.dirname(__file__))


def init_db():
    import kn.models
    import auth.models

    Base.metadata.create_all(bind=engine)
    print __name__, '>>create db'


def get_base_metadata():
    from kn.models import *
    from auth.models import *

    return Base.metadata


def autogenerate():
    'alembic revision --autogenerate -m "Added account table"'
    pass


def upgrade():
    'alembic upgrade head'
    pass


if __name__ == '__main__':
    init_db()
