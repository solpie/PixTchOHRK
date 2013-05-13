__author__ = 'SolPie'
from flask import (
    Blueprint,
    request,
    url_for,
    redirect,
    jsonify,
    render_template)
from flask.ext import login

route_home = Blueprint('home', __name__, template_folder='../templates/pixtch/')


@route_home.route('/')
def index():
    return render_template('index.html', uppo=login.current_user)


@route_home.route('/home')
def home():
    return redirect(url_for('.index'))


@route_home.route('/test/')
def test_view():
    return 'test'


@route_home.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('static/upload/upload.txt')
