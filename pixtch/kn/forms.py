# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from flask.ext import wtf
from flask.ext.uploads import UploadSet, IMAGES

images = UploadSet("images", IMAGES)


class KnForm(wtf.Form):
    title = wtf.TextField('title', validators=[wtf.required()])
    html_content = wtf.TextAreaField('content', validators=[wtf.required()])
    tags = wtf.SelectMultipleField(u'tags', choices=[('music', 'V+ music'), ('image', 'Painting'), ('pv', 'PV')])
    img = wtf.FileField('image', validators=[wtf.file_allowed(images, "Images only!")])