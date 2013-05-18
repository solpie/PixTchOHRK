from flask.ext.admin import BaseView, expose, AdminIndexView, Admin
from permissions import p_admin
from flask import url_for, Blueprint
from flask.ext.principal import Identity, Principal, RoleNeed, UserNeed, \
    Permission, identity_changed, identity_loaded
from flask.ext import login


class AdminView(AdminIndexView):
    @expose('/')
    # @p_admin.require()
    def index(self):
        return self.render('admin/index.html')


class BackendView(BaseView):
    def is_accessible(self):
        isAuth = login.current_user.is_authenticated()
        return isAuth

    @expose('/')
    @p_admin.require()
    def index(self):
        url = url_for('.test')
        print 'BackendView'
        # return self.render('index.html', url=url)
        return self.render('admin/index.html')

    @expose('/test/')
    def test(self):
        return self.render('pixtch/admin/index.html')


admin = Admin(name='Pixtch', index_view=AdminView())


def init_admin(app):
    # admin.add_view(BackendView(name='Pixtch Backend', endpoint='testadmin',url=))
    admin.base_template = 'admin/user/layout.html'
    # admin.index_view = AdminIndexView()
    from flask.ext.admin.contrib.fileadmin import FileAdmin

    import os

    path = os.path.join(app.config.root_path, 'static')
    admin.add_view(FileAdmin(path, '/static/', name='Static Files'))
    admin.init_app(app)
    return admin

