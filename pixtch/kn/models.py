# -*- coding:utf-8 -*-
from modules import db
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
    #ID
    id = db.Column(db.Integer, primary_key=True)
    #post_author
    author = db.Column(db.BIGINT(20), default=0)
    #post_date
    created = db.Column(db.DateTime, default=datetime.now)
    #post_date_gmt
    #post_content
    html_content = db.Column(db.TEXT)#allow uppo 自定义部分
    #post_title
    title = db.Column(db.Unicode(40))
    #post_excerpt
    #post_status
    status = db.Column(db.VARCHAR(20), default='publish')
    #comment_status
    comment_status = db.Column(db.VARCHAR(20), default='open')
    #ping_status
    ping_status = db.Column(db.VARCHAR(20), default='open')
    slug = db.Column(db.String(120))

    category_id = db.Column(db.Integer, db.ForeignKey(KnCategory.id))
    # category = sa.relationship(KnCategory, backref='posts')

    # owner = sa.Column(sa.ForeignKey(User))
    cover_url = db.Column(db.String(256))#封面图片
    modified = db.Column(db.DateTime, default=datetime.now)
    #view from user
    pv = db.Column(db.Integer, default=0)
    #every get request
    get_counts = db.Column(db.Integer, default=0)

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



