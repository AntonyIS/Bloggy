from flask import Flask

app = Flask(__name__)

# required routes
# /posts
# http://127.1.1.0:5000
@app.route('/')
def index():
	return "Hello world"

# /signup
# http://127.1.1.0:5000/signup
@app.route('/signup')
def signup():
	return "Signup page"

# /login
# http://127.1.1.0:5000/login
@app.route('/login')
def login():
	return "Login page"

# /account
# http://127.1.1.0:5000/login
@app.route('/account')
def account():
	return "account page"

# /posts/id
# http://127.1.1.0:5000/posts/121231232
@app.route('/posts/<int:post_id>')
def posts(post_id):
	return "Post detail page page"

# /posts/id
# http://127.1.1.0:5000/update/posts/121231232
@app.route('/posts/update/<int:post_id>')
def posts(post_id):
	return "Post update route"

# /posts/id
# http://127.1.1.0:5000/posts/delete/121231232
@app.route('/posts/update/<int:post_id>')
def posts(post_id):
	return "Post delete route"



if __name__ == "__main__":
	app.run(debug=True)