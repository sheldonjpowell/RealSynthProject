from flask import render_template, redirect, url_for, flash 
from flask_login import login_user, logout_user, login_required 
from . import auth 
from .forms import SignUpForm, LogInForm 
from .models import User

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    title = "Sign Up"
    form = SignUpForm()

    if form.validate_on_submit():
        email = form.email.data 
        username = form.username.data 
        password = form.password.data 

        # Check if user already exists 
        # .ilike() is case insensitive 
        user_already_exists = User.query.filter((User.username.ilike(username)) | (User.email.ilike(email))).all()
        if user_already_exists:
            # If taken, flash warning message, redirect
            flash("That username or email is already in use, please try again.", "danger")
            return render_template('signup.html', title=title, form=form)
        
        new_user = User(email = email, username = username, password = password)
        flash(f"{new_user} has been created!", "success")
        login_user(new_user)
        return redirect(url_for('index'))
    return render_template('signup.html', title = title, form = form)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    title = "Log In"
    form = LogInForm()

    if form.validate_on_submit():
        username = form.username.data 
        password = form.password.data 
        #Check for a user with that name 
        user = User.query.filter(User.username.ilike(username)).first()
        if user and user.check_password(password):
            login_user(user)
            flash(f"{user} has successfully logged in.", "success")
            return redirect(url_for('home.index'))
        else:
            flash("Username and/or password is incorrect.")
    return render_template('login.html', title = title, form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have successfully logged out.", "success")
    return redirect(url_for('home.index'))