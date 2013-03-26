#coding=utf-8
__author__ = 'SolPie'
from flask import Response, Blueprint
from flask.ext.principal import Principal, Permission, RoleNeed, PermissionDenied
from runserver import app

mod = Blueprint('auth', __name__)


# load the extension
principals = Principal(mod)

# Create a permission with a single Need, in this case a RoleNeed.
permission_admin = Permission(RoleNeed('admin'))
permission_uppo = Permission(RoleNeed('uppo'))


# protect a view with a principal for that need
@mod.route('/')
@permission_admin.require()
def do_admin_index():
    return Response('Only if you are an admin')

@app.route('/route_test')
def route_test():
    return Response('route test')

@mod.errorhandler(PermissionDenied)
def permissionDenied(error):
    print '该操作()需要的访问权限为:' + str(error.args[0].needs)
    return Response('Only if you are an admin')

# this time protect with a context manager
@mod.route('/articles')
def do_articles():
    with permission_admin.require():
        return Response('Only if you are admin')


