# -*- coding: utf-8 -*-
__author__ = 'SolPie'
import os
import json
import sys

sys.path.insert(0, os.path.join('.', 'pixtch'))
from runserver import app


@app.route('/env')
def env():
    return os.environ.get("VCAP_SERVICES", "{}")


def mysql_uri():
    local = os.environ.get("MONGODB", None)
    if local:
        return local
    services = json.loads(os.environ.get("VCAP_SERVICES", "{}"))
    if services:
        creds = services['mysql-5.1'][0]['credentials']
        uri = "mysql://%s:%s@%s:%d/%s" % (
            creds['username'],
            creds['password'],
            creds['hostname'],
            creds['port'],
            creds['db'])
        print >> sys.stderr, uri
        return uri
    else:
        raise Exception, "No services configured"


if __name__ == '__main__':
    app.init_db(mysql_uri)
    app.setup()
    app.run(debug=True)