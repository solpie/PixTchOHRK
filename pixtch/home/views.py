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
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    print request.remote_addr
    return jsonify(result=a + b)

# @app.errorhandler(404)
# def error404(error):
#     return render_template('404.html')


@route_home.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('static/upload/upload.txt')
