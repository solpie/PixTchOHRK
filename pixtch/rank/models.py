# -*- coding:utf-8 -*-
from modules import db
from datetime import datetime
from flask.ext.admin.contrib.sqlamodel import ModelView


class RankBase(object):
    id = db.Column(db.Integer, primary_key=True)
    #view from user
    pv = db.Column(db.Integer, default=0)
    #every get request
    get_counts = db.Column(db.Integer, default=0)

    ref_id = db.Column(db.Integer, default=0)

    def __init__(self, ref_id):
        self.ref_id = ref_id


class RankKnPost(RankBase, db.Model):
    __tablename__ = 'pt_rank_kn_post'

    def __init__(self, kn_post):
        super(RankKnPost, self).__init__(kn_post.id)
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



