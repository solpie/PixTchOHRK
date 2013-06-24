# -*- coding:utf-8 -*-
from flask.ext.admin.contrib.sqlamodel import ModelView

from modules import db
from kn.models import KnPost


class RankKnPost(db.Model):
    __tablename__ = 'pt_rank_kn_post'
    id = db.Column(db.Integer, db.ForeignKey(KnPost.id), primary_key=True)
    #view from user
    pv = db.Column(db.Integer, default=0)
    #every get request
    view_counts = db.Column(db.Integer, default=0)
    related_cls = db.relationship(KnPost)

    def __init__(self):
        super(RankKnPost, self).__init__()
        self.view_counts = 0
        self.pv = 0

    def __repr__(self):
        return '<RankKnPost %d>' % self.view_counts


class RankKnPostAdmin(ModelView):
    column_list = ('related_cls', 'pv', 'get_counts')
    column_labels = dict(related_cls='KnPost')
    # column_searchable_list = ('pv', User.name)
    # form_columns = ('title', 'html_content', 'status')


def add_admin(admin):
    admin.add_view(RankKnPostAdmin(RankKnPost, db.session, category='Rank'))



