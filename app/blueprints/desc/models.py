
from app import db
from datetime import datetime



class Presets(db.Model):
    id = db.Column(db.Integer, primary_key=True),
    volume = db.Column(db.Numeric, unique=False, nullable=False)
    octave = db.Column(db.Float, unique=False, nullable=False)
    attack = db.Column(db.Float, unique=False, nullable=False)
    decay = db.Column(db.Float, unique=False, nullable=False)
    sustain = db.Column(db.Numeric, unique=False, nullable=False)
    release = db.Column(db.Float, unique=False, nullable=False)
    waveforms = db.Column(db.Float, unique=False, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    save = db.Column(db.Float, unique=False, nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

