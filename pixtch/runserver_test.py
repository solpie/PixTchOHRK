__author__ = 'SolPie'
import os
import runserver
import unittest
import tempfile


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, runserver.app.config['DATABASE'] = tempfile.mkstemp()
        # app.app.config['TESTING'] = True
        self.app = runserver.app.test_client()
        runserver.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(runserver.app.config['DATABASE'])

    def test_addUser(self):
        from database import db_session
        from kn.models import User

        u = User('admin2', 'admin2@localhost')
        db_session.add(u)
        ret = db_session.commit()
        print ret


    def test_empty_db(self):
        rv = self.app.get('/show')
        assert 'No entries here so far' in rv.data

    # def test_messages(self):
    #     """Test that messages work"""
    #     self.login(runserver.app.config['USERNAME'],
    #                runserver.app.config['PASSWORD'])
    #     rv = self.app.post('/add', data=dict(
    #         title='<Hello>',
    #         text='<strong>HTML</strong> allowed here'
    #     ), follow_redirects=True)
    #     assert 'No entries here so far' not in rv.data
    #     assert '&lt;Hello&gt;' in rv.data
    #     assert '<strong>HTML</strong> allowed here' in rv.data

    def login(self, username, password):
        return self.app.post('/login', data=dict(username=username, password=password), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)


if __name__ == '__main__':
    unittest.main()