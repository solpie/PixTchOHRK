__author__ = 'SolPie'
from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Text


class Uppo(Base):
    __tablename__ = 'uppo'
    id = Column(Integer, primary_key=True)
    skill = Column(String)
    name_p = Column(String)
