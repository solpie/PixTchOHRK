#coding=utf-8
__author__ = 'SolPie'
from datetime import datetime
from modules import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.admin.contrib.sqlamodel import ModelView


class User(db.Model):
    __tablename__ = 'pt_users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(20))
    register_date = db.Column(db.DateTime, default=datetime.now)
    last_login_date = db.Column(db.DateTime)
    pw_hash = db.Column(db.String(256))
    active_key = db.Column(db.VARCHAR(60))

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        if password:
            self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def is_authenticated(self):
        # Flask-Login integration
        return True

    def is_active(self):
        # 未激活用户return False
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % self.name


# Customized User model admin
class UserAdmin(ModelView):
    list_template = 'admin/user/list.html'
    create_template = 'admin/user/create.html'
    edit_template = 'admin/user/edit.html'
    # Show only name and email columns in list view
    column_list = ('name', 'email', 'register_date', 'last_login_date')
    # Enable search functionality - it will search for terms in
    # name and email fields
    column_searchable_list = ('name', 'email')

    # Add filters for name and email columns
    column_filters = ('name', 'email')


def add_admin(admin):
    admin.add_view(UserAdmin(User, db.session, category='User'))
