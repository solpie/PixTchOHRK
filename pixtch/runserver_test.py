__author__ = 'SolPie'
import os
import runserver
import unittest
import tempfile

from database import db_session


class AppTestCase(unittest.TestCase):
    def setUp(self):
        # self.db_fd, runserver.app.config['DATABASE'] = tempfile.mkstemp()
        # app.app.config['TESTING'] = True
        self.app = runserver.app.test_client()
        runserver.init_database()
        # runserver.init_admin()
        # runserver.init_bluePrint()

    def tearDown(self):
        # os.close(self.db_fd)
        # os.unlink(runserver.app.config['DATABASE'])
        pass

    def test_addUser(self):
        from auth.models import User
        print User.query.filter(User.name == 'admin')
        if not User.query.filter(User.name == 'admin'):
            u = User('admin', 'admin@localhost', '-+')
            db_session.add(u)
            ret = db_session.commit()
            print 'create admin user'

    def test_kn_addTag(self):
        from kn.models import Tag

        tag = Tag()
        tag.name = 'tag test'
        db_session.add(tag)
        db_session.commit()

    def test_kn_addKnPost(self):
        from kn.models import KnPost

        knPost = KnPost("test")
        db_session.add(knPost)
        db_session.commit()

    def test_home(self):
        rv = self.app.get('/')
        assert 'home' in rv.data

    def test_kn_index(self):
        rv = self.app.get('/kn/')
        assert 'knnn' in rv.data

    def test_empty_db(self):
        # rv = self.app.get('/show')
        # assert 'No entries here so far' in rv.data
        pass

    def login(self, username, password):
        return self.app.post('/login', data=dict(username=username, password=password), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)


if __name__ == '__main__':
    unittest.main()