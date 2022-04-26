from flask_wtf import FlaskForm
from wtforms import DecimalRangeField, IntegerRangeField,SubmitField
from wtforms.validators import NumberRange

class SliderForm(FlaskForm):
    volume = DecimalRangeField('volume',validators=[NumberRange(min=0, max=.1)])
    octave = IntegerRangeField('octave',validators=[NumberRange(min=0, max=2)])
    attack = DecimalRangeField('attack',validators=[NumberRange(min=.001, max=.5)])
    decay = DecimalRangeField('decay',validators=[NumberRange(min=.001, max=.3)])
    sustain = IntegerRangeField('sustain',validators=[NumberRange(min=400, max=200000)])
    release = DecimalRangeField('release',validators=[NumberRange(min=0.5, max=2.5)])
    waveforms = DecimalRangeField('waveform',validators=[NumberRange(min=0, max=.75)])
    save = SubmitField('save')

   