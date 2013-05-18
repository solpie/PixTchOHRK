__author__ = 'SolPie'
from flask import (
    Blueprint,
    request,
    url_for,
    redirect,
    jsonify,
    render_template)
from flask.ext import login

bp = Blueprint('home', __name__, template_folder='../templates/pixtch/home')


@bp.route('/')
def index():
    return render_template('index.html', uppo=login.current_user)


@bp.route('/home')
@bp.route('/home/')
def home():
    return redirect(url_for('.index'))


@bp.route('/test/')
def test_view():
    return 'test'


# @route_home.route('/images/<regex("[a-zA-Z0-9]+.jpg"):img>')
@bp.route('/images/<regex(".+.jpg"):img>')
@bp.route('/images/<regex(".+.png"):img>')
@bp.route('/images/<regex(".+.gif"):img>')
def image(img):
    imgs = str(img)
    return redirect(url_for('static', filename='images/' + imgs))


@bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('static/upload/upload.txt')
