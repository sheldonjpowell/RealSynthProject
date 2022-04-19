from app import db, login
from flask_login import UserMixin 
from datetime import datetime 
from werkzeug.security import generate_password_hash, check_password_hash 

@login.user_loader
def get_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    email    = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(256), nullable = False)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    # my_cart = db.relationship('Cart', backref = 'mycart', lazy='dynamic')
    # my_listings = db.relationship('BookList', backref='mylisting', lazy='dynamic')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = generate_password_hash(kwargs['password'])
        db.session.add(self)
        db.session.commit() 

    def __repr__(self):
        return f"<User | {self.username}>"
    def __str__(self):
        return self.username

    def check_password(self, password):
        return check_password_hash(self.password, password)