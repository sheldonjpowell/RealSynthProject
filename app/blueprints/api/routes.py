from . import api
from flask import jsonify, request
from app.blueprints.auth.models import User


@api.route('/')
def index():
    return jsonify({'test': "this is a test"})


@api.route('/user')
def get_users():
    user = User.query.all()
    return jsonify([u.to_dict() for u in user])

@api.route('/signup', methods=['POST'])
def signup():
    data = request.json
    return 'Sign me up jonny up'