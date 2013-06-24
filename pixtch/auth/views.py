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
    jsonify,
    render_template)

from flask.ext.principal import Principal, Permission, RoleNeed, PermissionDenied, identity_changed, Identity, AnonymousIdentity
from flask.ext.login import (LoginManager, current_user, login_required,
                             login_user, logout_user, UserMixin,
                             confirm_login, fresh_login_required, logout_user)
from models import User
from forms import *
from modules import db
from datetime import datetime

from flask.ext.babelex import gettext, lazy_gettext as _


bp = Blueprint('auth', __name__, template_folder='../templates/pixtch/auth')
# load the extension
principals = Principal(bp)
# Create a permission with a single Need, in this case a RoleNeed.
permission_admin = Permission(RoleNeed('admin'))
permission_uppo = Permission(RoleNeed('uppo'))

login_manager = LoginManager()

# login_manager.anonymous_user = AnonymousUser


def init_auth(app):
    @app.errorhandler(PermissionDenied)
    def permissionDenied(error):
        print '该操作()需要的访问权限为:' + str(error.args[0].needs)
        return Response('Auth Only if you are an admin')
    login_manager.init_app(app)
    principals = Principal(app)


@login_manager.user_loader
def load_user(userid):
    # Return an instance of the User model
    user = User.query.get(userid)
    return user


def get_user(name):
    return User.query.filter(User.name == name).first()


@bp.route('/logout/')
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


@bp.route('/login', methods=['GET', 'POST'])
@bp.route('/login/', methods=['GET', 'POST'])
def auth():
    if request.method == 'GET':
        form = LoginForm(request.form)
        return render_template('login.html', form=form)
    #post
    name = request.values.get('name', type=str)
    password = request.values.get('pw', type=str)
    remember = request.values.get('rm', type=int)
    user = get_user(name)
    if user is None:
        return jsonify(error='Invalid user')
    if not user.check_password(password):
        return jsonify(error='Invalid password')
    login_user(user, remember)
    user.last_login_date = datetime.now()
    db.session.commit()
    identity_changed.send(current_app._get_current_object(), identity=Identity(user.id))
    print __name__, 'Login user ', current_user
    return jsonify(error='sus')
    # return jsonify(error='Invalid user')


@bp.route('/register/', methods=['GET', 'POST'])
@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        pw = form.password.data
        user = User(name, email, pw)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        print 'create admin user', user
        return redirect(url_for('.auth'))
    else:
        return render_template('register.html', form=form)


@bp.route('/activate/<act_key>')
def activate(act_key):
    return 'uppo %s' % act_key