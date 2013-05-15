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
    from bae.core.const import *

    user, pw, host, port, db = MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, 'MVwslEoiYLtUAerKTSuE'
    engine = create_engine('mysql://' + user + ':' + pw + '@' + host + ':' + port + '/' + db, convert_unicode=True,
                           echo=False)
    print "This is BAE environ"
else:
    engine = create_engine('sqlite:///db/test.db', convert_unicode=True, echo=False)
    print "This is local environ"
##################################################

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def session_add(base):
    db_session.add(base)


def session_commit():
    db_session.commit()


def connect(url):
    engine = create_engine(url, convert_unicode=True,
                           echo=False)
    create_db(engine)
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
