__author__ = 'SolPie'
from kn.models import KnPost
from rank.models import RankKnPost
from flask import Blueprint
bp = Blueprint('rank', __name__, template_folder='../templates/pixtch/')

@bp.route('/rank')
@bp.route('/rank/')
def rank_kn():
    rank = RankKnPost.query.order_by(RankKnPost.view_counts).all()
    return str(rank)