# pip install requests
# pip install lxml
from flask import Flask, request, render_template
import requests
from lxml import etree

app = Flask(__name__)

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
param = 'https://ip138.com/mobile.asp?mobile={tel}&action=mobile'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/search_phone')
def search_phone():
    tel = request.args.get('phone_number')
    resp = requests.get(param.format(tel=tel), headers=headers)
    resp.encoding = 'utf8'
    e = etree.HTML(resp.text)
    datas = e.xpath('//td[2]/span/text()')
    return '<br>'.join(datas)


app.run()