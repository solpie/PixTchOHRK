__author__ = 'SolPie'
from flask import Blueprint, render_template
from flask.ext.login import current_user, login_required

from models import Uppo


# bp = Blueprint('uppo', __name__)
bp = Blueprint('uppo', __name__, template_folder='../templates/pixtch/uppo')


def get_uppo(pid):
    return Uppo.query.get(pid)


@bp.route('/p/<int:pid>')
def uppo_view(pid):
    if pid:
        uppo = get_uppo(pid)
        return render_template('detail.html', uppo=uppo)
    else:
        render_template('list.html')

@bp.route('/dashboard')
@login_required
def uppo_home():
    uppo = current_user
    return render_template('dashboard.html', uppo=uppo)