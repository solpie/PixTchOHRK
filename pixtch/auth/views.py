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

from flask.ext.principal import Principal, Permission, RoleNeed, PermissionDenied, identity_changed, Identity, AnonymousIdentity
from flask.ext.login import (LoginManager, current_user, login_required,
                             login_user, logout_user, UserMixin, AnonymousUser,
                             confirm_login, fresh_login_required, logout_user)
from models import User
from forms import *
import database as db
from wtforms import ValidationError

route_auth = Blueprint('auth', __name__, template_folder='../templates/pixtch/auth')
# load the extension
principals = Principal(route_auth)
# Create a permission with a single Need, in this case a RoleNeed.
permission_admin = Permission(RoleNeed('admin'))
permission_uppo = Permission(RoleNeed('uppo'))

login_manager = LoginManager()

login_manager.anonymous_user = AnonymousUser


def init_auth(app):
    login_manager.init_app(app)
    principals = Principal(app)


@login_manager.user_loader
def load_user(userid):
    # Return an instance of the User model
    user = User.query.filter(User.id == userid).first()
    return user


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
    return redirect(url_for('home.index'))


@route_auth.errorhandler(PermissionDenied)
def permissionDenied(error):
    print '该操作()需要的访问权限为:' + str(error.args[0].needs)
    return Response('Auth Only if you are an admin')


@route_auth.route('/login/', methods=['GET', 'POST'])
def login_view():
    e = None
    form = LoginForm(request.form)
    print form.name.data, form.user
    # try:
    #     if form.validate_on_submit() and form.validate_login():
    #         user = form.get_user(form.name.data)
    #         ret = login_user(user)
    #         # user.set_password(user.password)
    #         # db.session_commit()
    #         print __name__, 'Loggin user ', ret, current_user
    #         # Tell Flask-Principal the identity changed
    #         identity_changed.send(current_app._get_current_object(), identity=Identity(user.id))
    #         return redirect('/')
    # except Exception, e:
    #     pass
    # return render_template('login.html', form=form, error=e)

    if form.validate_on_submit():
        try:
            form.validate_login()
        except ValidationError, e:
            return render_template('login.html', form=form, error=e)
        e = 'login'
        user = form.get_user(form.name.data)
        ret = login_user(user)
        # user.set_password(user.password)
        # db.session_commit()
        print __name__, 'Loggin user ', ret, current_user
        # Tell Flask-Principal the identity changed
        identity_changed.send(current_app._get_current_object(), identity=Identity(user.id))
        return redirect('/')
    else:
        return render_template('login.html', form=form, error=e)


@route_auth.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.name = form.name.data
        user.password = form.password.data
        db.session_add(user)
        db.session_commit()
        flash('Thanks for registering')
        print 'create admin user', user
        return redirect(url_for('.login_view'))
    else:
        return render_template('register.html', form=form)


@route_auth.route('/uppo/<upponame>')
def show_uppo_profile(upponame):
    return 'uppo %s' % upponame