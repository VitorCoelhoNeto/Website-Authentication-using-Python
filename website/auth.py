from flask import Blueprint, flash, render_template, request, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Renders the login page as well as its methods and routes.
    :return: render_template("login.html", user=current_user)
    :rtype: function
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(password)
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again!', category='error')
        else:
            flash('Incorrect email, try again!', category='error')

    return render_template("login.html", user=current_user)



@auth.route('/logout')
@login_required
def logout():
    """
    Logs the user out and redirects them to the login page.
    :return: redirect(url_for('auth.login'))
    :rtype: function
    """
    logout_user()
    return redirect(url_for('auth.login'))



@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    """
    Renders the sign up page as well as its methods and routes.
    :return: render_template("sign_up.html", user=current_user)
    :rtype: function
    """
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password = request.form.get('password')
        passwordConfirm = request.form.get('passwordConfirm')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists', category='error')
        elif len(email) < 4:
            flash("Email must be greater than 4 characters", category='error')
        elif len(first_name) < 2:
            flash("First name too short", category='error')
        elif password != passwordConfirm:
            flash("Passwords don't match", category='error')
        elif len(password) < 7:
            flash("Password too short ", category='error')
        else:
            newUser = User(email=email, first_name=first_name, password=generate_password_hash(password, method='sha256'))
            db.session.add(newUser)
            db.session.commit()
            login_user(newUser, remember=True)
            flash("Account created successfully!", category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)