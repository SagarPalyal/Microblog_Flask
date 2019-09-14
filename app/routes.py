from flask import render_template
from app import app

#using two decorators for index function
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Micky Mouse'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)