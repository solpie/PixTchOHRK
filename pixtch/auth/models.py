#coding=utf-8
__author__ = 'SolPie'
from sqlalchemy import Column, Integer, String, DateTime, Text
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(20))
    register_date = Column(DateTime)

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

        # Flask-Login integration

    def is_authenticated(self):
        return True
    # 未激活用户return False
    def is_active(self):
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