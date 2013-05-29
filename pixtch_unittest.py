__author__ = 'SolPie'
import sys
import os

sys.path.insert(0, os.path.join('.', 'pixtch'))
import unittest
from modules import db
import tempfile
from flaskPixtch import create_app


db_uri = 'sqlite:///db/unit_test.db'
app = create_app()
app.init_db(uri=db_uri)
app.setup()
db.app = app
db.init_app(app)
db.drop_all()
db.create_all()


class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        # app.testing = True
        app.config['TESTING'] = True
        print 'setup...'

    def tearDown(self):
        # os.close(self.db_fd)
        pass
        # os.unlink(flaskr.config['DATABASE'])

    def test_addUser(self):
        from auth.models import User

        email = app.config.get('ADMINS')[0]
        admin = User('admin', email, '-+')
        db.session.add(admin)
        db.session.commit()
        assert True

    def test_kn_addTag(self):
        from kn.models import Tag

        tag = Tag()
        tag.name = 'tag test'
        db.session.add(tag)
        db.session.commit()

    def test_kn_addKnPost(self):
        from kn.models import KnPost

        knPost = KnPost("test")
        db.session.add(knPost)
        db.session.commit()


class E_404TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        # app.testing = True
        app.config['TESTING'] = True

    def test_index(self):
        rv = self.app.get('/')
        assert 'Home' in rv.data

    def test_kn_post_list(self):
        rv = self.app.get('/kn/')
        assert 'knnn' in rv.data

    def test_kn_post_detail(self):
        rv = self.app.get('/kn/1')
        assert 'pv 1' in rv.data
        assert 'views 1' in rv.data

    def test_logout_anonymous(self):
        rv = self.app.get('/logout/')
        assert '401' in rv.data
        # rv = self.app.post('/login/', data={'name': 'admin', 'pw': '-+'})
        # rv = self.app.get('/logout/')
        # assert 'Home' in rv.data

    def test_login(self):
        rv = self.app.post('/login/', data={'name': 'admin', 'pw': '-+'})
        assert 'sus' in rv.data

    def test_logout_user(self):
        rv = self.app.get('/logout/')
        assert 'Home' in rv.data


if __name__ == '__main__':
    unittest.main()