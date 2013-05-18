__author__ = 'SolPie'
from module import db
from auth.models import User
from flask.ext.admin.contrib.sqlamodel import ModelView


class Uppo(db.Model):
    __tablename__ = 'pt_uppo'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('pt_users.id'))
    user = db.relation(User, backref=db.backref('pt_uppo', order_by=id))
    name_p = db.Column(db.String(20))
    sex = db.Column(db.Integer)
    birthday = db.Column(db.DateTime)
    cellphone = db.Column(db.Integer)
    name_real = db.Column(db.String(20))
    qq = db.Column(db.Integer)
    skill = db.Column(db.String(128))
    avatar = db.Column(db.String(256))
    weibo_id = db.Column(db.Integer)
    brief = db.Column(db.String(256))

    def __init__(self):
        pass

    def __repr__(self):
        return '<Uppo %r>' % self.name_p


class UppoAdmin(ModelView):
    column_list = ('user_id', 'name_p')


def add_admin(admin):
    admin.add_view(UppoAdmin(Uppo, db.session, category='User'))