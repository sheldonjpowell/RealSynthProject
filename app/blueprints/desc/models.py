
from flask_login import UserMixin
from app import db
from datetime import datetime



class Presets(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    volume = db.Column(db.Numeric(5), unique=False, nullable=False)
    octave = db.Column(db.Float(5), unique=False, nullable=False)
    attack = db.Column(db.Float(5), unique=False, nullable=False)
    decay = db.Column(db.Float(5), unique=False, nullable=False)
    sustain = db.Column(db.Numeric(10), unique=False, nullable=False)
    release = db.Column(db.Float(5), unique=False, nullable=False)
    waveforms = db.Column(db.Float(5), unique=False, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit() 


    def delete(self):
        # when delete button is clicked  and you have a preset selected 

        db.session.delete(self)
        db.session.commit() 

    def update(self):
        db.session.update()


