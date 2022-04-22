from flask import Blueprint

desc = Blueprint('desc', __name__, url_prefix='/desc')

from . import routes