#coding=utf-8
__author__ = 'SolPie'
from flask import (
    Response,
    Blueprint,
    current_app,
    request,
    url_for,
    flash,
    redirect,
    render_template)

from flask.ext import wtf, login
from flask.ext.principal import Principal, Permission, RoleNeed, PermissionDenied, identity_changed, Identity
from flask.ext.login import (LoginManager, current_user, login_required,
                             login_user, logout_user, UserMixin, AnonymousUser,
                             confirm_login, fresh_login_required)
from .models import User


route_auth = Blueprint('auth', __name__, template_folder='templates/pixtch')
# load the extension
principals = Principal(route_auth)
# Create a permission with a single Need, in this case a RoleNeed.
permission_admin = Permission(RoleNeed('admin'))
permission_uppo = Permission(RoleNeed('uppo'))

login_manager = LoginManager()
login_manager.init_app(route_auth)

login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(userid):
    # Return an instance of the User model
    return User.query.all()

#
@route_auth.route('/logout/')
def logout():
    identity_changed.send(current_app, identity=AnonymousIdentity())
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

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
@route_auth.route('/test')
def do_articles():
    with permission_admin.require():
        return Response('Only if you are admin')


# Define login and registration forms (for flask-login)
class LoginForm(wtf.Form):
    name = wtf.TextField(validators=[wtf.required()])
    password = wtf.PasswordField(validators=[wtf.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise wtf.ValidationError('Invalid user')

        if user.password != self.password.data:
            raise wtf.ValidationError('Invalid password')

    def get_user(self):
        name = str(self.name.data)
        print 'get user :' + name
        return User.query.filter(User.name == name).first()


@route_auth.route('/login/', methods=['GET', 'POST'])
def login_view():
    e = None
    form = LoginForm(request.form)
    if form.validate_on_submit():
        e = 'login'
        user = form.get_user()
        print 'form.get_user()', user
        # login_user(user)
        return redirect(url_for('/'))
    else:
        return render_template('pixtch/login_form.html', form=form, error=e)


def login():
    error = None
    config = dict()
    config['USERNAME'] = 'admin'
    config['PASSWORD'] = '-+'
    print User.query.all()
    if request.method == 'POST':
        formUserName = request.form['username']
        formPassWord = request.form['password']
        if User.query.filter(User.name == formUserName):
            rs = User.query.filter(User.name == formUserName).first()
            print rs.name, rs.password
        if formUserName != config['USERNAME']:
            error = 'Invalid username'
        elif formPassWord != config['PASSWORD']:
            error = 'Invalid password'
        else:
            identity_changed.send(current_app._get_current_object(), identity=Identity(request.form['username']))
            # session['logged_in'] = True
            #flash('You were logged in')
            #return redirect(url_for('show_entries'))
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



