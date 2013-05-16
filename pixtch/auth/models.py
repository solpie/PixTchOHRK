#coding=utf-8
__author__ = 'SolPie'
from sqlalchemy import Column, Integer, String, DateTime, Text
from database import Base
from datetime import datetime
from database import db
from werkzeug.security import generate_password_hash, check_password_hash

# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), unique=True)
#     email = db.Column(db.String(120), unique=True)
#     password = db.Column(db.String(20))
#     register_date = db.Column(db.DateTime, default=datetime.now)
#     last_login_date = db.Column(db.DateTime)
#     pw_hash = db.Column(db.String(256))

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(20))
    register_date = Column(DateTime, default=datetime.now)
    last_login_date = Column(DateTime)
    pw_hash = Column(String(256))

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
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

    @staticmethod
    def get(id=None, name=None):
        if id:
            return User.query.filter(User.id == id)
        if name:
            return User.query.filter(User.name == name)

    def __repr__(self):
        return '<User %r>' % self.name