from flask import render_template
from app import app

@app.route('/') #Decorators (modifies the function)
@app.route('/index') # Common to use decorators to register functions as callbacks for events

def index():
    user = {'username':'Joan Jose Lora'}
    posts = [
        {
            'author': {'username': 'Anwar'},
            'body' : 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Frank'},
            'body' : 'The Last of Us is so good!'
        }
    ]
    return render_template('index.html', title = 'Home', user=user, posts = posts)
