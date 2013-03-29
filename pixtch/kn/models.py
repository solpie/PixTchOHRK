# -*- coding:utf-8 -*-
import sqlalchemy as sa
from database import Base
from auth.models import User


class KnCategory(Base):
    __tablename__ = 'kn_category'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.String(40)

    def __init__(self, name):
        self.name = name
        pass

class KnPost(Base):
    __tablename__ = 'kn_post'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(40))
    slug = sa.Column(sa.String(120))
    category = sa.ForeignKey(KnCategory)
    html_content = sa.String#allow uppo 自定义部分
    owner = sa.ForeignKey(User)
    status = sa.Integer
    created = sa.DateTime
    modified = sa.DateTime
    pv = sa.Integer

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<KnPost %r>2' % self.title



