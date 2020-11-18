from flask import render_template, url_for, flash, redirect
from injections import app, db, bcrypt
from injections.models import User
from injections.forms import RegistrationForm, LoginForm
from flask_login import login_user

@app.route("/", methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
            flash('You have been logged in!', 'success')
            return redirect(url_for('success'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('index.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.email.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Fill This Out', form=form)


@app.route("/success", methods=['GET', 'POST'])
def success():
    return render_template('success.html', title='Good Job')
