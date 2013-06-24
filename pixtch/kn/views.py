__author__ = 'SolPie'
import hashlib
import tempfile
import os

from flask import Blueprint, render_template, abort, request, redirect, flash
from jinja2 import TemplateNotFound
from flask.ext.login import login_required, current_user
from werkzeug.utils import secure_filename

from models import KnPost
from forms import KnForm
from modules import db
from rank.models import RankKnPost


bp = Blueprint('kn', __name__, url_prefix='/kn', template_folder='../templates/pixtch/kn')


@bp.route('/<int:kid>')
def show_kn_post(kid):
    try:
        kn = KnPost.query.filter_by(id=kid).first()
        rank = RankKnPost.query.filter_by(id=kn.id).first()
        if not rank:
            rank = RankKnPost()
            rank.related_cls = kn
            db.session.add(rank)
        rank.view_counts += 1# (rank.view_counts + 1) or 0
        if not current_user.is_anonymous():#todo pv views one user one count
            rank.pv += 1
        db.session.commit()#todo database when to sync
        return render_template('detail.html', kn=kn, rank=rank)
    except TemplateNotFound:
        # abort(404)
        pass


@bp.route('/')
def show():
    try:
        kn = KnPost.query.order_by(KnPost.id)
        return render_template('list.html', kn_list=kn)
    except TemplateNotFound:
        abort(404)
        pass


@bp.route('/add_kn_post/', methods=['GET', 'POST'])
@login_required
def add_kn_post():
    form = KnForm(request.form)
    if form.validate_on_submit():
        kn = KnPost()
        kn.title = unicode(form.title.data)
        kn.html_content = form.html_content.data
        if form.img.name:
            img_file = request.files[form.img.name]
            if img_file.filename:
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
        return render_template('form.html', form=form)
    pass


@bp.route('/upload/<kn_type>', methods=['GET', 'POST'])
@login_required
def upload(kn_type):
    form = KnForm(request.form)
    if request.method == 'GET':
        return render_template('form.html', form=form)

    if kn_type == 'music':
        return 'is music'
    if kn_type == 'lyric':
        return 'is lyric'
    if kn_type == 'photo':
        img = request.files[form.img.name]
        data = img.file.read()
        tmp = tempfile.mkstemp()
        md5 = hashlib.md5()
        md5.update(data)
        md5num = md5.hexdigest()
        f = os.fdopen(tmp[0], 'wb+')
        f.write(data)
        f.close()
        return 'is photo'