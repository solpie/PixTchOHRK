# -*- coding: utf-8 -*-
__author__ = 'SolPie'
import sae
import sys

sys.path.insert(0, '.')
from pixtch.runserver import app
application = sae.create_wsgi_app(app)
app.main()