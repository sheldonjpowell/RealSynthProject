from app import app, db 
from app.blueprints.auth.models import User 

@app.shell_context_processor 
def make_context():
    return {'db':db, 'User':User}