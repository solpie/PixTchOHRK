#coding=utf-8
__author__ = 'SolPie'
from flask import Response, Blueprint
from flask.ext.principal import Principal, Permission, RoleNeed, PermissionDenied

app = Blueprint('auth', __name__)


# load the extension
principals = Principal(app)

# Create a permission with a single Need, in this case a RoleNeed.
permission_admin = Permission(RoleNeed('admin'))
permission_uppo = Permission(RoleNeed('uppo'))


# protect a view with a principal for that need
@app.route('/')
@permission_admin.require()
def do_admin_index():
    return Response('Only if you are an admin')


@app.errorhandler(PermissionDenied)
def permissionDenied(error):
    print '该操作()需要的访问权限为:' + str(error.args[0].needs)
    return Response('Only if you are an admin')

# this time protect with a context manager
@app.route('/articles')
def do_articles():
    with permission_admin.require():
        return Response('Only if you are admin')