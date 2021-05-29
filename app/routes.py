from app import app
from flask import render_template, flash, redirect, url_for
from app import app
from app.form import LoginForm


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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request from user {}, remember_me {}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)