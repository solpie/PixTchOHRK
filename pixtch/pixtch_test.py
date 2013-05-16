__author__ = 'SolPie'
import runserver
import unittest
import tempfile
from runserver import app
from flaskPixtch import Pixtch
from flask.ext.testing import TestCase
import database as db


class PixtchTest(TestCase):
    def create_app(self):
        app = Pixtch('test')
        app.config['TESTING'] = True
        return app

    def setUp(self):
        from database import create_db

        create_db()
        pass

    def test_login(self):
        response = self.client.get

    def tearDown(self):
        # os.close(self.db_fd)
        # os.unlink(runserver.app.config['DATABASE'])
        pass

    #
# class AppTestCase(unittest.TestCase):
#     def setUp(self):
#         self.db_fd, runserver.app.config['DATABASE'] = tempfile.mkstemp()
#         runserver.app.config['TESTING'] = True
#         self.app = runserver.app.test_client()
#         # runserver.init_Path()
#         runserver.init_database()
#         # runserver.init_bluePrint()
#         # runserver.init_ext()
#
#     def tearDown(self):
#         # os.close(self.db_fd)
#         # os.unlink(runserver.app.config['DATABASE'])
#         pass
#
#     def test_addUser(self):
#         from auth.models import User
#
#         print User.query.filter(User.name == 'admin')
#         if not User.query.filter(User.name == 'admin'):
#             u = User('admin', 'admin@localhost', '-+')
#             db.session_add(u)
#             db.session_commit()
#             print 'create admin user'
#
#     def test_kn_addTag(self):
#         from kn.models import Tag
#
#         tag = Tag()
#         tag.name = 'tag test'
#         db.session_add(tag)
#         db.session_commit()
#
#     def test_kn_addKnPost(self):
#         from kn.models import KnPost
#
#         knPost = KnPost("test")
#         db.session_add(knPost)
#         db.session_commit()
#
#     def test_home(self):
#         rv = self.app.get('/')
#         assert 'Home' in rv.data
#
#     def test_kn_index(self):
#         rv = self.app.get('/kn/')
#         assert 'knnn' in rv.data


if __name__ == '__main__':
    unittest.main()