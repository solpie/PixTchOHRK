from flask.ext.admin import BaseView, expose

from flask import url_for, Blueprint
from flask.ext.principal import Identity, Principal, RoleNeed, UserNeed, \
    Permission, identity_changed, identity_loaded
from flask.ext import login


route_admin = Blueprint('adminbackend', __name__)
permission_admin = Permission(RoleNeed('admin'))


class BackendView(BaseView):
    def is_accessible(self):
        isAuth = login.current_user.is_authenticated()
        return isAuth

    @expose('/')
    @permission_admin.require(401)
    def index(self):
        url = url_for('.test')
        print 'BackendView'
        # return self.render('index.html', url=url)
        return self.render('admin/index.html')

    @expose('/test/')
    def test(self):
        return self.render('pixtch/admin/index.html')


def init_admin(app):
    from module import admin

    admin.add_view(BackendView(name='Pixtch Backend', endpoint='testadmin'))

    from flask.ext.admin.contrib.fileadmin import FileAdmin

    import os

    path = os.path.join(app.config.root_path, 'static')
    admin.add_view(FileAdmin(path, '/static/', name='Static Files'))
    admin.init_app(app)

