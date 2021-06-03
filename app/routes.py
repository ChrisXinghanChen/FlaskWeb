from flask_login.utils import login_required, logout_user
from werkzeug.security import check_password_hash
from app.models import User
from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.form import LoginForm, RegistrationForm
from flask_login import current_user, login_user, login_required
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    
    posts = [
        {
            'author':{'userName': 'Chris'},
            'body':'I love Tia!'
        },
        {
            'author':{'userName': 'Tia'},
            'body':'I love Chris!'
        }
    ]
    return render_template('index.html', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = url_for('index')
        if not next_page or url_parse(next_page).netloc != '':
            return redirect(next_page)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registerd user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)