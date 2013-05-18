__author__ = 'SolPie'
from flask import Flask, render_template
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, map, *args):
        self.map = map
        self.regex = args[0]


class Pixtch(Flask):
    def __init__(self, name):
        super(Pixtch, self).__init__(name)

    def setup(self):
        self.init_path()
        self.init_ext()
        self.init_app()
        self.init_error()

    def init_db(self, uri=None):
        if uri:
            self.config['SQLALCHEMY_DATABASE_URI'] = uri
        pass

    def init_app(self):
        self.url_map.converters['regex'] = RegexConverter
        self.init_module('home')
        self.init_module('auth')
        self.init_module('uppo')
        self.init_module('kn')

    def init_module(self, module):
        try:
            m = __import__(module + '.models')
            m.models.add_admin(self.admin)
        except ImportError, e:
            print 'module [', module, '] do not have models'

        try:
            v = __import__(module + '.views')
            # v.views.bp.template_folder = 'templates/pixtch/' + module
            self.register_blueprint(v.views.bp)
        except ImportError, e:
            print 'module [', module, '] do not have views'

    def init_path(self):
        import sys
        import os
        import pprint

        # pprint.pprint(('[path]', __name__, self.config.root_path, sys.path))

    def init_error(self):
        @self.errorhandler(404)
        def error404(e):
            return render_template('404.html', e=e)

        @self.errorhandler(401)
        def error401(e):
            return render_template('401.html', e=e)

        from module import db

        @self.before_request
        def before_request():
            pass

        @self.teardown_request
        def shutdown_session(exception=None):
            db.session.remove()
            # print __name__, '>>shutdown_session'
            pass

    def init_ext(self):
        from admin.views import init_admin
        from auth.views import init_auth
        from flask.ext.bootstrap import Bootstrap

        self.admin = init_admin(self)
        init_auth(self)
        Bootstrap(self)


def create_app(db=None, uri=None):
    app = Pixtch(__name__)
    app.config.from_pyfile('settings.py')
    if db and uri:
        app.init_db(uri=uri)
        db.init_app(app)
        app.setup()
        # db.create_all(app=app)
    return app

    # @app.route('/view/<regex("[a-zA-Z0-9]+"):uuid>/')
    # def view(uuid):
    #     """
    #     url: /view/1010000000125259/
    #     result: view uuid:1010000000125259
    #     """
    #     return "view uuid: %s" % (uuid)
    #
    #
    # @app.route('/<regex(".*"):url>')
    # def not_found(url):
    #     """
    #     url: /hello
    #     result: not found: 'hello'
    #     """
    #     return "not found: '%s'" % (url)
    #
    #
    # if __name__ == '__main__':
    #     app.run()