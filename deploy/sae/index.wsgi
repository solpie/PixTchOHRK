import sae
import sys
import os

sys.path.insert(0, '.')
sys.path.insert(0, os.path.join(os.path.split(os.path.realpath(__file__))[0],'site-packages'))
sys.path.insert(0, os.path.join('.', 'site-packages'))
from runserver import app

application = sae.create_wsgi_app(app)
