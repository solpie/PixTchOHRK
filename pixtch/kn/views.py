__author__ = 'SolPie'
from flask import Blueprint, render_template, abort, session, request, redirect, flash, url_for
from jinja2 import TemplateNotFound

app = Blueprint('kn', __name__)


@app.route('/<int:kid>')
def show_kn_post(kid):
    return 'keng %d' % kid

from pixtch.auth.views import permission_admin
@app.route('/')
# @permission_admin.require()
def show():
    try:
        return render_template('pixtch/kn/show.html')
    except TemplateNotFound:
        # abort(404)
        pass


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)', [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))
