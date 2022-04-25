from . import api
from .auth import basic_auth, token_auth
from flask import jsonify, request
from app.blueprints.auth.models import User


@api.route('/token')
@basic_auth.login_required
def index():
    user = basic_auth.current_user()
    token = user.get_token()
    return jsonify({'token': token, 'expiration': user.token_expiration})

# create user
@api.route('/user/create', methods=['POST'])
def create_user():
    if not request.is_json:
        return jsonify({'error': 'Your request content-type must be application/json'})
    data = request.json
    for feild in ['username', 'email', 'password']:
        if feild not in data:
            return jsonify({'error':f'{feild} must be in request body'}), 400
    username = data['username']
    email = data['email']
    password = data['password']
    user_with_that_info = User.query.filter((User.username==username)|(User.email==email)).all()
    if user_with_that_info:
        return jsonify({'error': 'A user with that username and/or email already exists'})
    new_user = User(username=username, email=email, password=password)
    return jsonify(new_user.to_dict()),201


@api.route('/user')
def get_users():
    user = User.query.all()
    return jsonify([u.to_dict() for u in user])

@api.route('/signup', methods=['POST'])
# @token_auth.login_required
def signup():
    data = request.json
    return 'Sign me up jonny up'

# @api.route()