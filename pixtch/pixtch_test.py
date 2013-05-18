__author__ = 'SolPie'
import unittest
from flask.ext.testing import TestCase
from module import db

import os
import unittest
import tempfile


class PixtchTestCase(unittest.TestCase):
    def setUp(self):
        from flaskPixtch import create_app
        from module import db

        db_uri = 'sqlite:///db/unit_test.db'
        pixtch = create_app(db, db_uri)
        self.db_fd, pixtch.config['DATABASE'] = tempfile.mkstemp()
        pixtch.config['TESTING'] = True
        self.app = pixtch.test_client()

    def test_index(self):
        rv = self.app.get('/')
        assert 'Home' in rv.data

    def tearDown(self):
        os.close(self.db_fd)
        # os.unlink(flaskr.config['DATABASE'])

    def test_addUser(self):
        from auth.models import User
        print User.query.filter(User.name == 'admin')
        if not User.query.filter(User.name == 'admin'):
            u = User('admin', 'admin@localhost', '-+')
            db.session.add(u)
            db.session.commit()
            print 'create admin user'
        pass

    def test_kn_addTag(self):
        from kn.models import Tag

        tag = Tag()
        tag.name = 'tag test'
        db.session_add(tag)
        db.session_commit()

    def test_kn_addKnPost(self):
        from kn.models import KnPost

        knPost = KnPost("test")
        db.session_add(knPost)
        db.session_commit()

    def test_home(self):
        rv = self.app.get('/')
        assert 'Home' in rv.data

    def test_kn_index(self):
        rv = self.app.get('/kn/')
        assert 'knnn' in rv.data


if __name__ == '__main__':
    unittest.main()