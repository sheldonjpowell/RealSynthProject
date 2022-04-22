from . import desc
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
    title = 'synth'

    return render_template('synth.html', title = title)