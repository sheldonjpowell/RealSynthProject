from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import LoginManager 
from config import Config 

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)
# compare_type=True
# Leave this when modifying the database, otherwise it doesn't recognize small changes

login = LoginManager(app)
login.login_view = 'auth.login' # Set this to your login page
login.login_message_category = 'danger'

from app.blueprints.auth import auth 
app.register_blueprint(auth)

from app.blueprints.home import home 
app.register_blueprint(home)

from app import routes