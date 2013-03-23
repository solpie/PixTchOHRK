__author__ = 'SolPie'
from pixtch.db.database import db


class Kn(db.model):
    id = db.Column(db.Integer, primary_key=True)
    pub_date = db.Column(db.DateTime)
    title = db.Column(db.String(120))
    slug = db.Column(db.String(120))
    text = db.Column(db.Text)
    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.username