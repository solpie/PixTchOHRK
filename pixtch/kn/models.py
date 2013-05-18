# -*- coding:utf-8 -*-
from module import db
from datetime import datetime
from flask.ext.admin.contrib.sqlamodel import ModelView
from auth.models import User


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


class KnPostAdmin(ModelView):
    column_list = ('title', 'created', 'modified')
    # column_list = ('title', ('owner', User.name), 'created', 'modified')
    column_searchable_list = ('title', User.name)
    form_columns = ('title', 'html_content', 'status')


def add_admin(admin):
    admin.add_view(KnPostAdmin(KnPost, db.session, category='Kn'))
    admin.add_view(ModelView(Tag, db.session, category='Kn'))



