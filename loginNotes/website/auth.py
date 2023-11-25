from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()

        if user:
            check_password_hash(user.password, password)
            flash('Logged in Successfully', category='success')
        else:
            flash('Incorrect email or password, try again', category='error')

    else:
        flash('Email doesn\'t exist.', category='error')


    return render_template('login.html', boolean=True)


@auth.route('/logout')
def logout():
    return "<p> Logout </p>"


@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        data = request.form
        email = data['email']
        password1 = data['password1']
        password2 = request.form.get('password2')
        firstName = request.form.get('firstName')


        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists', category='error')

        elif len(email) < 4:
            flash('Email must be grater than 3 characters.', category="error")

        elif len(firstName) < 2:
            flash('First Name must be grater than 1 characters.', category="error")

        elif password1 != password2:
            flash('Passwords must be equals.', category="error")

        elif len(password1)< 6:
            flash('Password must be greater than 5 characters.', category="error")

        else:
            new_user = User(email=email, first_name=firstName, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!.', category="success")

            return redirect(url_for('views.home'))

        print( f"{firstName}, {email} - {password1} wants to sign up." )
    return render_template('sign_up.html')