__author__ = 'SolPie'
from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relation, backref
from auth.models import User


class Uppo(Base):
    __tablename__ = 'uppo'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relation(User, backref=backref('uppo', order_by=id))
    name_p = Column(String)
    sex = Column(Integer)
    birthday = Column(DateTime)
    cellphone = Column(Integer)
    name_real = Column(String)
    qq = Column(Integer)
    skill = Column(String)
    avatar = Column(String)
    weibo_id = Column(Integer)
    brief = Column(String)


    def __repr__(self):
        return '<Uppo %r>' % self.name_p