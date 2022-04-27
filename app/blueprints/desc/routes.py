from crypt import methods
import wave
from . import desc
from .forms import SliderForm
from flask_login import login_required, current_user
from .models import Presets
from app.blueprints.auth.models import User
from flask import render_template

@desc.route('/')
def index():
    title = 'Home'

    return render_template('index.html', title = title)

@desc.route('/about')
def about():
    title = 'about'

    return render_template('about.html', title = title)

    
    
@desc.route('/synth', methods = ['GET', 'POST'])
@login_required 
def synth():
    # Presets = {}
    title = 'synth'
    form = SliderForm()

    if form.validate_on_submit():
        print('sup')
        volume = form.volume.data
        octave = form.octave.data
        attack = form.attack.data
        decay = form.decay.data
        sustain = form.sustain.data
        release = form.release.data
        waveforms = form.waveforms.data
        save = form.save.data
        apply = form.apply.data
        delete = form.delete.data
        print("sup")
        print(f'Save: {save} Apply: {apply} Delete: {delete}')
        if save == True:
            user = User.query.first()
            p = Presets(user_id=current_user.id, volume=volume, octave=octave, attack=attack, decay=decay, sustain=sustain, release= release, waveforms=waveforms)
            a = user.preset.all()
            print(a)
            # print(p, volume, octave, attack, decay, sustain,release,waveforms)
        elif apply == True:
            
            user = User.query.first()

        elif delete == True:
            p = Presets(user_id=current_user.id, volume=volume, octave=octave, attack=attack, decay=decay, sustain=sustain, release= release, waveforms=waveforms)
            print(p.query.filter_by())
    

    preset = current_user.preset.all()
    print(preset)

    return render_template('synth_test.html', title = title, form=form, preset=preset)