#coding=utf-8
__author__ = 'SolPie'
from flask import Response, Blueprint, current_app, request, render_template
from flask.ext.principal import Principal, Permission, RoleNeed, PermissionDenied, identity_changed, Identity

route_auth = Blueprint('auth', __name__)
# load the extension
principals = Principal(route_auth)

# Create a permission with a single Need, in this case a RoleNeed.
permission_admin = Permission(RoleNeed('admin'))
permission_uppo = Permission(RoleNeed('uppo'))


# @route_auth.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if USERS.get(username) is None:
#             error = 'Invalid username'
#         elif USERS.get(username) != password:
#             error = 'Invalid password'
#         else:
#             identity_changed.send(app, identity=Identity(request.form['username']))
#
#             session['logged_in'] = True
#             flash('You were logged in')
#             return redirect(url_for('show_entries'))
#     return render_template('login.html', error=error)
#
# @app.route('/logout')
# def logout():
#     identity_changed.send(app, identity=AnonymousIdentity())
#
#     session.pop('logged_in', None)
#     flash('You were logged out')
#     return redirect(url_for('show_entries'))

# protect a view with a principal for that need
# @route_auth.route('/')
# @permission_admin.require()
# def do_admin_index():
#     return Response('Only if you are an admin')

@route_auth.errorhandler(PermissionDenied)
def permissionDenied(error):
    print '该操作()需要的访问权限为:' + str(error.args[0].needs)
    return Response('Auth Only if you are an admin')

# this time protect with a context manager
@route_auth.route('/articles')
def do_articles():
    with permission_admin.require():
        return Response('Only if you are admin')


@route_auth.route('/login2', methods=['GET', 'POST'])
def login():
    error = None
    config = dict()
    config['USERNAME'] = 'admin'
    config['PASSWORD'] = '-+'
    if request.method == 'POST':
        if request.form['username'] != config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != config['PASSWORD']:
            error = 'Invalid password'
        else:
            identity_changed.send(current_app, identity=Identity(request.form['username']))
            #     session['logged_in'] = True
            # flash('You were logged in')
            #     return redirect(url_for('show_entries'))
    return render_template('pixtch/login.html', error=error)

#
#
# @app.route('/logout')
# def logout():
#     session.pop('logged_in', None)
#     flash('You were logged out')
#     return redirect(url_for('show_entries'))
#
# @identity_loaded.connect_via(app)
# def on_identity_loaded(sender,identity):
#     identity.provides.add(permission_admin)



