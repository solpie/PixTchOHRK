__author__ = 'SolPie'
from flask.ext.admin import Admin


class Admin(Admin):
    def __init__(self, app):
        super(Admin, self).__init__(app)