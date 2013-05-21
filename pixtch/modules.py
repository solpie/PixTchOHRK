__author__ = 'SolPie'
# -*- coding:utf-8 -*-
#####################SQLAlchemy##################
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


######################


# from flask.ext.admin import Admin
#
# admin = Admin()


def autogenerate():
    'alembic revision --autogenerate -m "Added account table"'
    pass


def upgrade():
    'alembic upgrade head'
    pass


if __name__ == '__main__':
    pass
