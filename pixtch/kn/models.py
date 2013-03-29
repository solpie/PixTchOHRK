# -*- coding:utf-8 -*-
import sqlalchemy as sa
from database import Base
from auth.models import User


class Tag(Base):
    __tablename__ = 'kn_tag'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Unicode(64))

    # Required for administrative interface
    def __unicode__(self):
        return self.name


class KnCategory(Base):
    __tablename__ = 'kn_category'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Unicode(40)

    def __init__(self, name):
        self.name = name
        pass


class KnPost(Base):
    __tablename__ = 'kn_post'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.Unicode(40))
    slug = sa.Column(sa.String(120))
    category = sa.ForeignKey(KnCategory)
    html_content = sa.String#allow uppo 自定义部分
    owner = sa.ForeignKey(User)
    status = sa.Integer
    created = sa.DateTime
    modified = sa.DateTime
    pv = sa.Integer

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<KnPost %r>2' % self.title



