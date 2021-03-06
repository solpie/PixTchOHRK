# -*- coding: utf-8 -*-
__author__ = 'SolPie'
DEBUG = True
SECRET_KEY = 'interesting'

SQLALCHEMY_DATABASE_URI = 'sqlite:///db/unit_test.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///db/test.db'
SQLALCHEMY_ECHO = False

UPLOADS_DEFAULT_DEST = '/static/'
UPLOADS_DEFAULT_URL = '/static'

CACHE_TYPE = "simple"
CACHE_DEFAULT_TIMEOUT = 300

THEME = 'default'

USE_LOCAL_COMMENT = True # if false, to include comment.html

ACCEPT_LANGUAGES = ['en', 'zh']

BABEL_DEFAULT_LOCALE = 'zh'
BABEL_DEFAULT_TIMEZONE = 'Asia/Shanghai'

PER_PAGE = 20

DEBUG_LOG = 'logs/debug.log'
ERROR_LOG = 'logs/error.log'

ADMINS = ('admin@pixtch.com',)

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = DEBUG
MAIL_USERNAME = 'username'
MAIL_PASSWORD = 'password'
DEFAULT_MAIL_SENDER = 'yourname@domain.com'