from werkzeug.security import check_password_hash
from app.models import User
from app import app
from flask import render_template, flash, redirect, url_for
from app.form import LoginForm
from flask_login import current_user, login_user


@app.route('/index')
def index():
    user = {'userName': 'Chris'}
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
    return render_template('index.html', user=user, posts=posts)


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
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)