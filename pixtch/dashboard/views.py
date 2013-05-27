__author__ = 'SolPie'
from flask import Blueprint, render_template, abort, session, request, redirect, flash, url_for
from jinja2 import TemplateNotFound
from models import KnPost
from modules import db
from flask.ext.login import login_required
from werkzeug.utils import secure_filename
import hashlib
import tempfile
import os

bp = Blueprint('dashboard', __name__, template_folder='../templates/pixtch/dashboard')


# @bp.route('/dashboard')
# def dashboard():
#         pass

