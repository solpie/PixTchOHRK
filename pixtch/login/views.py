#coding=utf-8
__author__ = 'SolPie'
from flask import Flask, Response, Blueprint
from flask.ext.principal import Principal, Permission, RoleNeed, PermissionDenied

app = Blueprint('login', __name__)


# load the extension
principals = Principal(app)

# Create a permission with a single Need, in this case a RoleNeed.
admin_permission = Permission(RoleNeed('admin'))

# protect a view with a principal for that need
@app.route('/')
@admin_permission.require()
def do_admin_index():
    return Response('Only if you are an admin')


@app.errorhandler(PermissionDenied)
def permissionDenied(error):
    print '该操作()需要的访问权限为:' + str(error.args[0].needs)
    return Response('Only if you are an admin')

# this time protect with a context manager
@app.route('/articles')
def do_articles():
    with admin_permission.require():
        return Response('Only if you are admin')