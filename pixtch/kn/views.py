__author__ = 'SolPie'
from flask import Blueprint, render_template, abort, session, request, redirect, flash, url_for
from jinja2 import TemplateNotFound
from models import KnPost
from forms import *
from module import db
from flask.ext.login import login_required
from werkzeug.utils import secure_filename

bp = Blueprint('kn', __name__,url_prefix='/kn')


@bp.route('/<int:kid>')
def show_kn_post(kid):
    try:
        kn = KnPost.query.filter(KnPost.id == kid).first()
        return render_template('pixtch/kn/detail.html', kn=kn)
    except TemplateNotFound:
        # abort(404)
        pass


@bp.route('/')
# @admin.require(401)
def show():
    try:
        kn = KnPost.query.order_by(KnPost.id)
        return render_template('pixtch/kn/list.html', kn_list=kn)
    except TemplateNotFound:
        abort(404)
        pass


@bp.route('/add_kn_post/', methods=['GET', 'POST'])
@login_required
def add_kn_post():
    form = KnForm(request.form)
    if form.validate_on_submit():
        kn = KnPost()
        kn.title = form.title.data
        kn.html_content = form.html_content.data
        if form.img.name:
            img_file = request.files[form.img.name]
            img_filename = secure_filename(img_file.filename)
            img_file.save('static/upload/' + img_filename)
        kn.status = 1
        db.session.add(kn)
        db.session.commit()
        flash('Thanks for posting')
        url = '/kn/' + str(kn.id)
        return redirect(url)
        pass
    else:
        return render_template('pixtch/kn/form.html', form=form)
    pass