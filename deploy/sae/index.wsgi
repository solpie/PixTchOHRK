import sys
import os

sys.path.insert(0, '.')
sys.path.insert(0, os.path.join(os.path.split(os.path.realpath(__file__))[0],'site-packages'))
sys.path.insert(0, os.path.join('.', 'site-packages'))
sys.path.insert(0, os.path.join('.', 'pixtch'))

from sae.const import (MYSQL_HOST, MYSQL_HOST_S,
                       MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB)

uri = "mysql://%s:%s@%s:%d/%s" % (
    MYSQL_USER,
    MYSQL_PASS,
    MYSQL_HOST,
    int(MYSQL_PORT),
    MYSQL_DB)

os.environ.setdefault('MYSQL', uri)

from runserver import app
app.setup()

import sae
application = sae.create_wsgi_app(app)
