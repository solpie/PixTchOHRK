from flask.ext.admin import Admin

from flask import Flask, Request, Response, url_for, render_template, request, session, flash, redirect, Blueprint
from flask.ext.principal import Identity, Principal, RoleNeed, UserNeed, \
    Permission, identity_changed, identity_loaded


mod = Blueprint('adminbackend', __name__)
permission_admin = Permission(RoleNeed('admin'))


def init(app):
    admin = Admin(app, name='Pixtch Backend')
    from database import db_session

    from flask.ext.admin.contrib.sqlamodel import ModelView
    from auth.models import User
    admin.add_view(ModelView(User, db_session))
    #
    from kn.models import KnPost, KnCategory, Tag
    admin.add_view(ModelView(Tag, db_session))
    from flask.ext.admin.contrib.fileadmin import FileAdmin

    import os
    path = os.path.join(app.config.root_path, 'static')
    admin.add_view(FileAdmin(path, '/static/', name='Static Files'))

# class Backend(AdminIndexView):
#     def __init__(self):
#         super(Backend, self).__init__()
#
#     @expose('/')
#     def index(self):
#         return self.render(self._template)

