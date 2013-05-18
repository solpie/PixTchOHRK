# -*- coding:utf-8 -*-
from database import db
from datetime import datetime


class Tag(db.Model):
    __tablename__ = 'pt_kn_tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))

    # Required for administrative interface
    def __unicode__(self):
        return self.name


class KnCategory(db.Model):
    __tablename__ = 'pt_kn_category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(40))

    def __init__(self, name):
        self.name = name
        pass


class KnPost(db.Model):
    __tablename__ = 'pt_kn_post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(40))
    slug = db.Column(db.String(120))

    category_id = db.Column(db.Integer, db.ForeignKey(KnCategory.id))
    # category = sa.relationship(KnCategory, backref='posts')

    html_content = db.Column(db.String(360))#allow uppo 自定义部分
    # owner = sa.Column(sa.ForeignKey(User))
    cover_url = db.Column(db.String(256))#封面图片
    status = db.Column(db.Integer)
    created = db.Column(db.DateTime)
    modified = db.Column(db.DateTime, default=datetime.now)
    pv = db.Column(db.Integer)

    def __init__(self, title=None):
        self.title = title

    def __repr__(self):
        return '<KnPost %r>' % self.title



