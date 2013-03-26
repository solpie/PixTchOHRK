from flask.ext.admin import Admin
from flask import Flask, Request, Response, url_for, render_template, request, session, flash, redirect, Blueprint
from flask.ext.principal import Identity, Principal, RoleNeed, UserNeed, \
    Permission, identity_changed, identity_loaded
from pixtch.runserver import app


mod = Blueprint('adminbackend', __name__)
permission_admin = Permission(RoleNeed('admin'))

# class Backend(AdminIndexView):
#     def __init__(self):
#         super(Backend, self).__init__()
#
#     @expose('/')
#     def index(self):
#         return self.render(self._template)


# @mod.route('/')
# def index():
#     """
#
#     Args:
#
#
#     Returns:
#
#     """
#     return Response('index')

