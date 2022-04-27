from app import app, db 
from app.blueprints.auth.models import User 
from app.blueprints.desc.models import Presets 

@app.shell_context_processor 
def make_context():
    return {'db':db, 'User':User, 'Presets':Presets}
    # 'Presets':Presets