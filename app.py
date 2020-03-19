from flask import Flask,render_template

app = Flask(__name__)

# required routes
# /posts
# http://127.1.1.0:5000
@app.route('/')
def index():
	title  = "Covid-19 | Home "
	return render_template('index.html', title = title)

# /signup
# http://127.1.1.0:5000/signup
@app.route('/signup')
def signup():
	title = "Covid-19 |Signup "
	return render_template('signup.html',title = title)

# /login
# http://127.1.1.0:5000/login
@app.route('/login')
def login():
	title = "Covid-19 | Login "
	return render_template('login.html',title = title)

# /account
# http://127.1.1.0:5000/login
@app.route('/account')
def account():
	title = "Covid-19 | Account "
	return render_template('account.html',title = title)

# /posts/id
# http://127.1.1.0:5000/posts/121231232
@app.route('/posts/<int:post_id>')
def post_detail(post_id):
	title = "Covid-19 | Post Detail "
	return render_template('post_detail.html',title = title)

# /posts/id
# http://127.1.1.0:5000/update/posts/121231232
@app.route('/posts/update/<int:post_id>')
def post_update(post_id):

	return "Post update route"

# /posts/id
# http://127.1.1.0:5000/posts/delete/121231232
@app.route('/posts/delete/<int:post_id>')
def post_delete(post_id):
	return "Post delete route"



if __name__ == "__main__":
	app.run(debug=True)