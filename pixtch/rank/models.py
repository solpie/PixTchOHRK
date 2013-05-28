# -*- coding:utf-8 -*-
from modules import db
from datetime import datetime
from flask.ext.admin.contrib.sqlamodel import ModelView
from kn.models import KnPost


class RankBase(object):
    id = db.Column(db.Integer, primary_key=True)
    #view from user
    pv = db.Column(db.Integer, default=0)
    #every get request
    get_counts = db.Column(db.Integer, default=0)

    ref_cls = None


    def __init__(self, ref_cls):
        if ref_cls:
            self.ref_cls = db.relationship(ref_cls)
        pass


class RankKnPost(RankBase, db.Model):
    __tablename__ = 'pt_rank_kn_post'
    id = db.Column(db.Integer, db.ForeignKey(KnPost.id), primary_key=True)
    ref_cls = db.relationship(KnPost)

    def __init__(self, kn_post=None):
        super(RankKnPost, self).__init__(None)
        self.get_counts = 0
        self.pv = 0

    def __repr__(self):
        return '<KnPost %r>' % self.title


class RankKnPostAdmin(ModelView):
    column_list = ('pv', 'get_counts')
    # column_list = ('title', ('owner', User.name), 'created', 'modified')
    # column_searchable_list = ('pv', User.name)
    # form_columns = ('title', 'html_content', 'status')


def add_admin(admin):
    admin.add_view(RankKnPostAdmin(RankKnPost, db.session, category='Rank'))



