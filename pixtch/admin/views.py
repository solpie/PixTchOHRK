from flask.ext.admin import Admin
from flask import Flask, Request, Response, url_for, render_template, request, session, flash, redirect, Blueprint
from flask.ext.principal import Identity, Principal, RoleNeed, UserNeed, \
    Permission, identity_changed, identity_loaded
from pixtch.runserver import app


mod = Blueprint('adminbackend', __name__)
permission_admin = Permission(RoleNeed('admin'))

# class Backend(AdminIndexView):
#     def __init__(self):
#         super(Backend, self).__init__()
#
#     @expose('/')
#     def index(self):
#         return self.render(self._template)


@mod.route('/')
def index():
    """

    Args:


    Returns:

    """
    return Response('index')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('pixtch/login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

@identity_loaded.connect_via(app)
def on_identity_loaded(sender,identity):
    identity.provides.add(permission_admin)
