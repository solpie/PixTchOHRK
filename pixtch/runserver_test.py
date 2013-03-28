__author__ = 'SolPie'
import os
import runserver
import unittest
import tempfile


class AppTestCase(unittest.TestCase):
    def setUp(self):
        # self.db_fd, runserver.app.config['DATABASE'] = tempfile.mkstemp()
        # app.app.config['TESTING'] = True
        self.app = runserver.app.test_client()
        # runserver.init_database()
        # runserver.init_admin()
        # runserver.init_bluePrint()

    def tearDown(self):
        # os.close(self.db_fd)
        # os.unlink(runserver.app.config['DATABASE'])
        pass

    def test_addUser(self):
        from database import db_session
        from auth.models import User
        # db_session
        # u = User('admin2', 'admin2@localhost')
        # db_session.add(u)
        # ret = db_session.commit()


    def test_home(self):
        rv = self.app.get('/')
        assert 'jinja2' in rv.data

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