# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from flask.ext import wtf


class KnForm(wtf.Form):
    title = wtf.TextField('title', validators=[wtf.required()])
    html_content = wtf.TextField('content', validators=[wtf.required()])