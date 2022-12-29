from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/index')
def index():
	username=request.args.get('username')
	return render_template('index.html',username=username)


@app.route('/login')
def login():
	return render_template('login.html')


app.run()