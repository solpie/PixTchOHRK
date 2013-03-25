__author__ = 'SolPie'
from sqlalchemy import Column, Integer, String, DateTime, Text
from database import Base



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    pub_date = Column(DateTime)
    title = Column(String(120))
    slug = Column(String(120))
    text = Column(Text)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>2' % self.name