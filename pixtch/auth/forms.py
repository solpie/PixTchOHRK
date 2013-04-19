# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from flask.ext import wtf
from models import User


class RegistrationForm(wtf.Form):
    name = wtf.TextField('uppo name', validators=[wtf.required()])
    email = wtf.TextField('Email Address', [wtf.validators.Length(min=6, max=35)])
    password = wtf.PasswordField('New Password', [
        wtf.validators.Required(),
        wtf.validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = wtf.PasswordField('Repeat Password')
    accept_tos = wtf.BooleanField('I accept the TOS', [wtf.validators.Required()])

    def validate_signup(self, field):
        name = self.name.data
        password = self.password.data
        print self, 'validate sign up'
        if name is None:
            raise wtf.ValidationError('no name')
        if User.query.filter(User.name == name):
            raise wtf.ValidationError('name is exist')
        pass


# Define login and registration forms (for flask-login)
class LoginForm(wtf.Form):
    name = wtf.TextField('uppo name', validators=[wtf.required()])
    password = wtf.PasswordField('password', validators=[wtf.required()])

    user = None

    def validate_login(self, field):
        self.user = user = self.get_user(self.name.data)
        print 'validate_login:', self.name.data, user
        if user is None:
            raise wtf.ValidationError('Invalid user')
        if user.password != self.password.data:
            raise wtf.ValidationError('Invalid password')
        return True

    def get_user(self, name):
        # name = str(self.name.data)
        user = User.query.filter(User.name == name).first()
        print 'query user :', name, 'result:', user
        return user