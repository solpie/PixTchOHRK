# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from flask.ext import wtf
from models import User


class RegistrationForm(wtf.Form):
    name = wtf.TextField('uppo name', validators=[wtf.required()])
    email = wtf.TextField('Email Address', validators=[wtf.validators.Length(min=6, max=35), wtf.validators.Email()])
    password = wtf.PasswordField('New Password', [
        wtf.validators.Required(),
        wtf.validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = wtf.PasswordField('Repeat Password')

    def validate_signup(self, field):

        name = self.name.data
        password = self.password.data
        print self, 'validate sign up'
        if name is None:
            raise wtf.ValidationError('no name')
        if User.query.filter(User.name == name):
            raise wtf.ValidationError('name is exist')
        pass

    def __call__(self, *args, **kwargs):
        self.email.widget.html_params('class=d')
        return super(RegistrationForm, self).__call__(args, kwargs)


class InputBlock(wtf.Input):
    def __init__(self, input_type=None):
        super(InputBlock, self).__init__(input_type)

    def __call__(self, field, **kwargs):
        kwargs.setdefault('class', "input-block-level")
        kwargs['placeholder'] = field.label.text
        return super(InputBlock, self).__call__(field, **kwargs)

        # Define login and registration forms (for flask-login)


class LoginForm(wtf.Form):
    name = wtf.TextField('uppo name', validators=[wtf.required()], widget=InputBlock('text'))
    password = wtf.TextField('password', validators=[wtf.required()], widget=InputBlock('password'))

    user = None

    def validate_login(self):
        self.user = user = self.get_user(self.name.data)
        print 'validate_login:', self.name.data, user
        if user is None:
            raise wtf.ValidationError('Invalid user')
        if not user.check_password(self.password.data):
            raise wtf.ValidationError('Invalid password')
        return True

    def get_user(self, name):
        # name = str(self.name.data)
        user = User.query.filter(User.name == name).first()
        print 'query user :', name, 'result:', user
        return user

