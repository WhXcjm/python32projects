# -*- coding: utf-8 -*-
# Flask

from flask import Flask,render_template
import random
app = Flask(__name__)

lis=['卡牌大师','德邦总管','无畏战车','诡术妖姬','猩红收割者','远古恐惧','正义天使','无极剑圣','牛头酋长','符文法师','亡灵战神','战争女神','众星之子']

@app.route('/index')
def index():
    return render_template('index.html',hero=lis)

@app.route('/choujiang')
def choujiang():
	return render_template('index.html',hero=lis,h=random.choice(lis))
app.run(debug=True)