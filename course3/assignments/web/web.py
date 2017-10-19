# from video tutorial https://www.youtube.com/watch?v=ZVGwqnjOKjk
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'

app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)


#log in, log out from https://pythonspot.com/en/login-authentication-with-flask/
@app.route('/')
def index():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return 'This is the homepage- Please log in'

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
	return posts()
    else:
        flash('wrong password!')
    return index()

@app.route ('/posts')
def posts():
	if session.get('logged_in'):
		posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
		posts.sort(key=lambda item:item['date'], reverse=True)
		return render_template('posts.html', posts=posts)
	else:
		return index()

@app.route('/posts/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)

@app.route ('/profile/<username>')
def profile(username):
	return render_template("profile.html",username=username)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()

if __name__=="__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True)
