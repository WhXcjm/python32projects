from flask import Flask,render_template,request

app=Flask(__name__)
data=[
	{'id':1,'name':'春节','likes':0},
	{'id':2,'name':'中秋','likes':0},
	{'id':3,'name':'端午','likes':0},
	{'id':4,'name':'元旦','likes':0},
	{'id':5,'name':'国庆','likes':0}
]
@app.route('/index')
def index():
	return render_template('index.html',data=data)

@app.route('/dianzan')
def dianzan():
	id=request.args.get('id')
	print(f"add 1 like to {id}")
	data[int(id)-1]['likes']+=1
	# return "点赞成功"
	return render_template('index.html',data=data)
app.run(debug=True)