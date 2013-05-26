__author__ = 'SolPie'
from flask import Blueprint, render_template, request
from models import Uppo
from forms import UpgradeForm

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


@bp.route('/upgrade', methods=['GET', 'POST'])
def upgrade2uppo():
    if request.method == 'GET':
        return render_template('upgrade.html')

    form = UpgradeForm
    uppo = Uppo()



