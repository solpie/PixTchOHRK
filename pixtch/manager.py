__author__ = 'SolPie'
from flask import Blueprint

bp = Blueprint('testbp', __name__)


@bp.route('/testbp')
def bptest():
    print 'test bp'
    return "test bp"