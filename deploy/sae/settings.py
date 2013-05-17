# -*- coding: utf-8 -*-
__author__ = 'SolPie'
DEBUG = True
SECRET_KEY = 'interesting'
from sae.const import (MYSQL_HOST, MYSQL_HOST_S,
                       MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB)

uri = "mysql://%s:%s@%s:%d/%s" % (
    MYSQL_USER,
    MYSQL_PASS,
    MYSQL_HOST,
    int(MYSQL_PORT),
    MYSQL_DB)

SQLALCHEMY_DATABASE_URI = uri
SQLALCHEMY_ECHO = False

UPLOADS_DEFAULT_DEST = '/path/to/pypress/static/'
UPLOADS_DEFAULT_URL = '/static'

CACHE_TYPE = "simple"
CACHE_DEFAULT_TIMEOUT = 300

THEME = 'default'

USE_LOCAL_COMMENT = True # if false, to include comment.html

ACCEPT_LANGUAGES = ['en', 'zh']

BABEL_DEFAULT_LOCALE = 'zh'
BABEL_DEFAULT_TIMEZONE = 'Asia/Shanghai'

# http://twitter.com/oauth_clients/new
TWITTER_KEY = ''
TWITTER_SECRET = ''

PER_PAGE = 20

DEBUG_LOG = 'logs/debug.log'
ERROR_LOG = 'logs/error.log'

ADMINS = ('yourname@domain.com',)

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = DEBUG
MAIL_USERNAME = 'username'
MAIL_PASSWORD = 'password'
DEFAULT_MAIL_SENDER = 'yourname@domain.com'