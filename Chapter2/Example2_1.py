from flask import Flask
from flask import render_template

app = Flask(__name__)

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