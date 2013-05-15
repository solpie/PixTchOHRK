# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from bae.core.wsgi import WSGIApplication

import sys
import os

sys.path.insert(0, os.path.join('.', 'site-packages'))
from runserver import app
from bae.core.const import *

# app.init_db(MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, 'MVwslEoiYLtUAerKTSuE')
application = WSGIApplication(app)
