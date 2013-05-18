__author__ = 'SolPie'
import unittest
from module import db
import tempfile
from flaskPixtch import create_app

app = create_app()


class PixtchTestCase(unittest.TestCase):
    def setUp(self):
        db_uri = 'sqlite:///db/unit_test.db'
        app.testing = True
        self.app = app.test_client()
        app.init_db(uri=db_uri)
        db.init_app(app)
        db.create_all(app=app)
        app.setup()

        self.db_fd = tempfile.mkstemp()
        app.config['TESTING'] = True

    def test_index(self):
        rv = self.app.get('/')
        assert 'Home' in rv.data

    def tearDown(self):
        # os.close(self.db_fd)
        pass
        # os.unlink(flaskr.config['DATABASE'])

    def test_addUser(self):
        from auth.models import User

        user = User.query.filter_by(name='admin')
        if not user:
            u = User('admin', 'admin@localhost', '-+')
            db.session.add(u)
            db.session.commit()
            print 'create admin user'
        pass

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

    def test_home(self):
        rv = self.app.get('/')
        assert 'Home' in rv.data

    def test_kn_index(self):
        rv = self.app.get('/kn/')
        assert 'knnn' in rv.data


if __name__ == '__main__':
    unittest.main()