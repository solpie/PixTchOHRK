__author__ = 'SolPie'
from flask.ext import wtf


class UpgradeForm(wtf.Form):
    name_p = wtf.TextField('p name', validators=[wtf.required()])
    sex = wtf.TextField('sex')
    birthday = wtf.DateField('birthday')
    qq = wtf.IntegerField('qq')
    skill = wtf.SelectMultipleField('pick up your skill')
    avatar = wtf.FileField('avatar')
    brief  = wtf.TextAreaField('brief')