__author__ = 'SolPie'
from modules import db
from auth.models import User
from flask.ext.admin.contrib.sqlamodel import ModelView


class Uppo(db.Model):
    __tablename__ = 'pt_uppo'
    id = db.Column(db.Integer, db.ForeignKey(User.id), primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('pt_users.id'))
    # user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)
    # user = db.relation(User, backref=db.backref('pt_uppo', order_by=id))
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

    def __init__(self, name_p=None, sex=None,
                 birthday=None, cellphone=None, name_real=None,
                 qq=None, skill=None, avatar=None,
                 weibo_id=None, brief=None):
        self.name_p = name_p
        self.sex = sex
        self.birthday = birthday
        self.cellphone = cellphone
        self.name_real = name_real
        self.qq = qq
        self.skill = skill
        self.avatar = avatar
        self.weibo_id = weibo_id
        self.brief = brief

    def __repr__(self):
        return '<Uppo %r>' % self.name_p


class UppoAdmin(ModelView):
    # inline_models = (Uppo,)
    # column_list = ('id', 'user', 'name_p')
    pass


def add_admin(admin):
    admin.add_view(UppoAdmin(Uppo, db.session, category='User'))