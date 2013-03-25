from flask.ext.admin import Admin
from flask import Flask, Request, Response, url_for, render_template, request, session, flash, redirect, Blueprint

app = Blueprint('adminbackend', __name__)


# class Backend(AdminIndexView):
#     def __init__(self):
#         super(Backend, self).__init__()
#
#     @expose('/')
#     def index(self):
#         return self.render(self._template)




@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('pixtch/login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
