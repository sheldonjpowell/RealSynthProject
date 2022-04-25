from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import LoginManager
from flask_cors import CORS 
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

CORS(app)

from app.blueprints.auth import auth 
app.register_blueprint(auth)

from app.blueprints.api import api 
app.register_blueprint(api)

from app.blueprints.desc import desc 
app.register_blueprint(desc)

from app import routes