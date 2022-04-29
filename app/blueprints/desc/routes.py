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
    preset = Presets.query.first()
    
    # presets = Presets.query.get(id)
    # volume = form.volume.data
    # octave = form.octave.data
    # attack = form.attack.data
    # decay = form.decay.data
    # sustain = form.sustain.data
    # release = form.release.data
    # waveforms = form.waveforms.data


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
        # delete = form.delete.data
        dropdown = int(form.dropdown.data)
        # print(decay)
        
        print(f'Save: {save}, Apply: {apply}')
        if save == True:
            user = User.query.first()
            check = Presets.query.filter_by(user_id = current_user.id).filter_by(preset_number=dropdown).first()
           
            
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
            preset =Presets.query.filter((Presets.preset_number==form.dropdown.data) & (Presets.user_id==current_user.id)).first()

        else:
            p = Presets(user_id=current_user.id, volume=volume, octave=octave, attack=attack, decay=decay, sustain=sustain, release= release, waveforms=waveforms, preset_number=dropdown)
            

            # p = Presets(user_id=current_user.id, volume=volume, octave=octave, attack=attack, decay=decay, sustain=sustain, release= release, waveforms=waveforms, preset_number=dropdown)



        # elif delete == True:
        #     check = Presets.query.filter_by(user_id = current_user.id).filter_by(preset_number=dropdown).first()
           
            
        #     if check:
        #         check.volume=volume 
        #         check.octave=octave 
        #         check.attack=attack 
        #         check.decay=decay 
        #         check.sustain=sustain
        #         check.release=release
        #         check.waveforms=waveforms
        #         db.session.delete(check)
        #         db.session.commit()
        #         print(Presets.query.all)
        #     else:
        #         p = Presets(user_id=current_user.id, volume=volume, octave=octave, attack=attack, decay=decay, sustain=sustain, release= release, waveforms=waveforms, preset_number=dropdown)
    

    
    # presets = Presets.query.get()
    # print(preset)

    return render_template('synth_test.html', title = title, form=form, preset=preset)