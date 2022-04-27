from flask_wtf import FlaskForm
from wtforms import DecimalRangeField, IntegerRangeField,SubmitField,StringField, SelectField
from wtforms.validators import NumberRange,DataRequired
from .models import Presets

class SliderForm(FlaskForm):
    # username = StringField('username', validators=[DataRequired()])
    volume = DecimalRangeField('volume',validators=[NumberRange(min=0, max=.1)])
    octave = IntegerRangeField('octave',validators=[NumberRange(min=0, max=2)])
    attack = DecimalRangeField('attack',validators=[NumberRange(min=.001, max=.5)])
    decay = DecimalRangeField('decay',validators=[NumberRange(min=.001, max=.3)])
    sustain = IntegerRangeField('sustain',validators=[NumberRange(min=400, max=200000)])
    release = DecimalRangeField('release',validators=[NumberRange(min=0.5, max=2.5)])
    waveforms = DecimalRangeField('waveform',validators=[NumberRange(min=0, max=3 )])
    save = SubmitField('Save')
    apply = SubmitField('Apply')
    delete = SubmitField('Delete')
    dropdown = SelectField('Dropdown',choices=[('1','Preset1'),('2','Preset2'),('3','Preset3'),('4','Preset4'),('5','Preset5')])


# class UserDetails(Form):
#     group_id = SelectField(u'Group', coerce=int)


# def edit_user(request, id):
#     user = User.query.get(id)
#     form = UserDetails(request.POST, obj=user)
#     form.group_id.choices = [(g.id, g.name) for g in Group.query.order_by('name')]


def ApplyPresets(request, id):
    presets = Presets.query.get(id)
    form = SliderForm(request.POST, obj=presets)
    form.dropdown.choices = [(d.id, d.name) for d in Dropdown.query.order_by('name')]