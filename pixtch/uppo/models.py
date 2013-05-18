__author__ = 'SolPie'
from database import db
from auth.models import User


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