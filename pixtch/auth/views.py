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
    session,
    render_template)

from flask.ext import wtf
from flask.ext.principal import Principal, Permission, RoleNeed, PermissionDenied, identity_changed, Identity, AnonymousIdentity
from flask.ext.login import (LoginManager, current_user, login_required,
                             login_user, logout_user, UserMixin, AnonymousUser,
                             confirm_login, fresh_login_required, logout_user)
from .models import User
from database import db_session


route_auth = Blueprint('auth', __name__, template_folder='templates')
# route_auth = Blueprint('auth', __name__, template_folder='templates/pixtch')
# load the extension
principals = Principal(route_auth)
# Create a permission with a single Need, in this case a RoleNeed.
permission_admin = Permission(RoleNeed('admin'))
permission_uppo = Permission(RoleNeed('uppo'))

login_manager = LoginManager()

login_manager.anonymous_user = AnonymousUser


def init_auth(app):
    login_manager.init_app(app)


@login_manager.user_loader
def load_user(userid):
    # Return an instance of the User model
    return User.query.filter(id == userid).first()

#
@route_auth.route('/logout/')
@login_required
def logout():
    logout_user()
    # Remove session keys set by Flask-Principal
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)

    # Tell Flask-Principal the user is anonymous
    identity_changed.send(current_app._get_current_object(),
                          identity=AnonymousIdentity())

    flash('You were logged out')
    return redirect(url_for('index'))


@route_auth.errorhandler(PermissionDenied)
def permissionDenied(error):
    print '该操作()需要的访问权限为:' + str(error.args[0].needs)
    return Response('Auth Only if you are an admin')

# this time protect with a context manager
@route_auth.route('/test/')
def login_test2():
    return redirect(url_for('.login_view'))


# Define login and registration forms (for flask-login)
class LoginForm(wtf.Form):
    name = wtf.TextField('uppo name', validators=[wtf.required()])
    password = wtf.PasswordField('password', validators=[wtf.required()])

    user = None

    def validate_login(self, field):
        self.user = user = self.get_user(self.name.data)
        print 'validate_login:', self.name.data, user
        if user is None:
            raise wtf.ValidationError('Invalid user')
        if user.password != self.password.data:
            raise wtf.ValidationError('Invalid password')
        return True

    def get_user(self, name):
        # name = str(self.name.data)
        user = User.query.filter(User.name == name).first()
        print 'query user :', name, 'result:', user
        return user


@route_auth.route('/login/', methods=['GET', 'POST'])
def login_view():
    e = None
    form = LoginForm(request.form)
    print form.name.data, form.user
    # if form.validate_on_submit() and form.validate_login('d'):
    if form.validate_on_submit():
        e = 'login'
        user = form.get_user(form.name.data)
        print __name__, 'form.get_user()', user
        login_user(user)
        # Tell Flask-Principal the identity changed
        identity_changed.send(current_app._get_current_object(),
                              identity=Identity(user.id))

        return redirect('/admin')
        # return redirect(url_for('login_test2'))
    else:
        return render_template('pixtch/login_form.html', form=form, error=e)


class RegistrationForm(wtf.Form):
    name = wtf.TextField('uppo name', validators=[wtf.required()])
    email = wtf.TextField('Email Address', [wtf.validators.Length(min=6, max=35)])
    password = wtf.PasswordField('New Password', [
        wtf.validators.Required(),
        wtf.validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = wtf.PasswordField('Repeat Password')
    accept_tos = wtf.BooleanField('I accept the TOS', [wtf.validators.Required()])

    def validate_signup(self, field):
        name = self.name.data
        password = self.password.data
        print self, 'validate sign up'
        if name is None:
            raise wtf.ValidationError('no name')
        if User.query.filter(User.name == name):
            raise wtf.ValidationError('name is exist')
        pass


@route_auth.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.name = form.name.data
        user.password = form.password.data
        db_session.add(user)
        ret = db_session.commit()
        flash('Thanks for registering')
        print 'create admin user', user
        return redirect(url_for('.login_view'))
    else:
        return render_template('pixtch/register_form.html', form=form)

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



