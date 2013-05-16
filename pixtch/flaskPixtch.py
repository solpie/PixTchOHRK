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
        self.init_app()
        self.init_path()
        self.init_bluePrint()
        self.init_ext()
        self.init_error()

    def init_db(self):

        # from database import create_db
        #
        # create_db()
        pass

    def init_app(self):
        self.url_map.converters['regex'] = RegexConverter

    def init_path(self):
        import sys

        sys.path.insert(0, 'libs')
        print __name__, self.config.root_path

    def init_error(self):
        @self.errorhandler(404)
        def error404(e):
            return render_template('404.html', e=e)

        @self.errorhandler(401)
        def error401(e):
            return render_template('401.html', e=e)

    def init_bluePrint(self):
        from home.views import route_home
        from auth.views import route_auth
        from kn.views import route_kn
        from admin.views import route_admin as admin

        self.register_blueprint(route_home)
        self.register_blueprint(route_auth)
        self.register_blueprint(route_kn, url_prefix='/kn')
        self.register_blueprint(admin)

        from database import db_session

        @self.before_request
        def before_request():
            pass

        @self.teardown_request
        def shutdown_session(exception=None):
            db_session.remove()
            # print __name__, '>>shutdown_session'
            pass

    def init_ext(self):
        from admin.views import init_admin
        from auth.views import init_auth
        from flask.ext.bootstrap import Bootstrap

        init_auth(self)
        init_admin(self)
        Bootstrap(self)


def create_app():
    app = Pixtch(__name__)
    app.config.from_pyfile('settings.py')
    # app.config.from_object(__name__)
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