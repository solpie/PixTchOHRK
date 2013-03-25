__author__ = 'SolPie'
from flask.ext import babelex as babel
from flask.ext.babelex import gettext, ngettext, lazy_gettext, Babel


class Locale(Babel):
    def __init__(self, app):
        super(Locale, self).__init__(app)
        app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'