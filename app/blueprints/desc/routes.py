from crypt import methods
from . import desc
from app import db
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
# @desc.route('/synth/<preset_id>', methods = ['GET', 'POST'])
@login_required 
def synth():
    # print(preset_id)
    # Presets = {}
    title = 'synth'
    form = SliderForm()
    # presets = Presets.query.get(id)


    print('hello')
    if form.validate_on_submit():
        
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
        dropdown = int(form.dropdown.data)
        
        print(f'Save: {save} Apply: {apply} Delete: {delete}')
        if save == True:
            user = User.query.first()
            check = Presets.query.filter_by(user_id = current_user.id).filter_by(preset_number=dropdown).first()
            print(check,'SOMTHING RANDOM')
            if check:
                check.volume=volume 
                check.octave=octave 
                check.attack=attack 
                check.decay=decay 
                check.sustain=sustain
                check.release=release
                check.waveforms=waveforms
                db.session.commit()
            else:
                p = Presets(user_id=current_user.id, volume=volume, octave=octave, attack=attack, decay=decay, sustain=sustain, release= release, waveforms=waveforms, preset_number=dropdown)
                # a = user.preset.all()
            
            
            # print(p, volume, octave, attack, decay, sustain,release,waveforms)
        elif apply == True:
            
            user = User.query.first()

        elif delete == True:
            p = Presets(user_id=current_user.id, volume=volume, octave=octave, attack=attack, decay=decay, sustain=sustain, release= release, waveforms=waveforms)
            print(p.query.filter_by())
    

    preset = current_user.preset.all()
    # presets = Presets.query.get()
    print(preset)

    return render_template('synth_test.html', title = title, form=form, preset=preset)