__author__ = 'SolPie'
import os
import pixtch
import unittest
import tempfile


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, pixtch.app.config['DATABASE'] = tempfile.mkstemp()
        # app.app.config['TESTING'] = True
        self.app = pixtch.app.test_client()
        pixtch.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(pixtch.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/show')
        assert 'No entries here so far' in rv.data

    def test_messages(self):
        """Test that messages work"""
        self.login(pixtch.app.config['USERNAME'],
                   pixtch.app.config['PASSWORD'])
        rv = self.app.post('/add', data=dict(
            title='<Hello>',
            text='<strong>HTML</strong> allowed here'
        ), follow_redirects=True)
        assert 'No entries here so far' not in rv.data
        assert '&lt;Hello&gt;' in rv.data
        assert '<strong>HTML</strong> allowed here' in rv.data

    def login(self, username, password):
        return self.app.post('/login', data=dict(username=username, password=password), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)


if __name__ == '__main__':
    unittest.main()