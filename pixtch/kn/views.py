__author__ = 'SolPie'
from flask import Blueprint, render_template, abort, session, request, redirect, flash, url_for
from jinja2 import TemplateNotFound
from models import KnPost
from forms import *

route_kn = Blueprint('kn', __name__)


@route_kn.route('/<int:kid>')
def show_kn_post(kid):
    return 'keng %d' % kid


@route_kn.route('/')
# @admin.require(401)
def show():
    try:
        kn = KnPost.query.filter(KnPost.id ==1).first()
        return render_template('pixtch/kn/show.html',kn=kn)
    except TemplateNotFound:
        # abort(404)
        pass


@route_kn.route('/add_kn_post/', methods=['GET', 'POST'])
def add_kn_post():
    form = KnForm(request.form)
    if form.validate_on_submit():
        pass
    else:
        return render_template('pixtch/kn/show.html')
    pass


@route_kn.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)', [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))
