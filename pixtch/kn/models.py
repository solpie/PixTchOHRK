# -*- coding:utf-8 -*-
import sqlalchemy as sa
from database import Base


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
    name = sa.Column(sa.Unicode(40))

    def __init__(self, name):
        self.name = name
        pass


class KnPost(Base):
    __tablename__ = 'kn_post'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.Unicode(40))
    slug = sa.Column(sa.String(120))

    category_id = sa.Column(sa.Integer(), sa.ForeignKey(KnCategory.id))
    # category = sa.relationship(KnCategory, backref='posts')

    html_content = sa.Column(sa.String(360))#allow uppo 自定义部分
    # owner = sa.Column(sa.ForeignKey(User))
    status = sa.Column(sa.Integer())
    created = sa.Column(sa.DateTime())
    modified = sa.Column(sa.DateTime())
    pv = sa.Column(sa.Integer())

    def __init__(self, title=None):
        self.title = title

    def __repr__(self):
        return '<KnPost %r>2' % self.title



