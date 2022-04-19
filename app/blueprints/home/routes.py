from . import home
from flask import render_template

@home.route('/')
def index():
    title = 'Home'

    return render_template('index.html', title = title)
    