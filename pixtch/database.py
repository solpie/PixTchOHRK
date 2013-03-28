__author__ = 'SolPie'
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
engine = create_engine('sqlite:///db/test.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db', 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


def init_db():
    import kn.models
    import auth.models

    Base.metadata.create_all(bind=engine)

    # if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    #     api.create(SQLALCHEMY_MIGRATE_REPO, 'database reppsitory')
    #     api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    # else:
    #     api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))


# @app.route('/mongo')
def mongotest():
    from pymongo import Connection

    uri = mongodb_uri()
    conn = Connection(uri)
    coll = conn.db['ts']
    coll.insert(dict(now=int(time.time())))
    last_few = [str(x['now']) for x in coll.find(sort=[("_id", -1)], limit=10)]
    body = "\n".join(last_few)
    return Response(body, content_type="text/plain;charset=UTF-8")


def mongodb_uri():
    local = os.environ.get("MONGODB", None)
    if local:
        return local
    services = json.loads(os.environ.get("VCAP_SERVICES", "{}"))
    if services:
        creds = services['mongodb-1.8'][0]['credentials']
        uri = "mongodb://%s:%s@%s:%d/%s" % (
            creds['username'],
            creds['password'],
            creds['hostname'],
            creds['port'],
            creds['db'])
        print >> sys.stderr, uri
        return uri
    else:
        raise Exception, "No services configured"
