from flask.ext.admin import Admin, BaseView, expose

from flask import Flask, Request, Response, url_for, render_template, request, session, flash, redirect, Blueprint
from flask.ext.principal import Identity, Principal, RoleNeed, UserNeed, \
    Permission, identity_changed, identity_loaded
from flask.ext.admin.contrib.sqlamodel import ModelView
from flask.ext import login


route_admin = Blueprint('adminbackend', __name__)
permission_admin = Permission(RoleNeed('admin'))


class BackendView(BaseView):
    def is_accessible(self):
        isAuth = login.current_user.is_authenticated()
        return isAuth

    @expose('/')
    def index(self):
        url = url_for('.test')
        return self.render('index.html', url=url)
        # return self.render('pixtch/admin/index.html')

    @expose('/test/')
    def test(self):
        return self.render('pixtch/admin/index.html')


from auth.models import User
# Customized User model admin
class UserAdmin(ModelView):
    # Show only name and email columns in list view
    column_list = ('name', 'email', 'register_date', 'last_login_date')

    # Enable search functionality - it will search for terms in
    # name and email fields
    column_searchable_list = ('name', 'email')

    # Add filters for name and email columns
    column_filters = ('name', 'email')


class KnPostAdmin(ModelView):
    column_list = ('title', 'created', 'modified')
    # column_list = ('title', ('owner', User.name), 'created', 'modified')
    column_searchable_list = ('title', User.name)
    form_columns = ('title', 'html_content', 'status')


def init_admin(app):
    from database import db_session
    from kn.models import KnPost, KnCategory, Tag

    admin = Admin(name='Pixtch Backend')
    # admin = Admin(app, name='Pixtch Backend')
    admin.add_view(BackendView(name='Pixtch Backend'))
    admin.add_view(UserAdmin(User, db_session, category='User'))
    admin.add_view(KnPostAdmin(KnPost, db_session, category='Kn'))
    admin.add_view(ModelView(Tag, db_session, category='Kn'))

    from flask.ext.admin.contrib.fileadmin import FileAdmin

    import os

    path = os.path.join(app.config.root_path, 'static')
    admin.add_view(FileAdmin(path, '/static/', name='Static Files'))
    admin.init_app(app)

