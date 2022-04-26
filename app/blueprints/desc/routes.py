from . import desc
from .forms import SliderForm
from flask import render_template

@desc.route('/')
def index():
    title = 'Home'

    return render_template('index.html', title = title)

@desc.route('/about')
def about():
    title = 'about'

    return render_template('about.html', title = title)
    
@desc.route('/synth')
def synth():
    # Presets = {}
    title = 'synth'
    form = SliderForm()
    

    return render_template('synth_test.html', title = title, form=form)