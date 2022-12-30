import requests
import json
from lxml import etree
from time import sleep
home='https://movie.douban.com/j/search_subjects?type=movie&tag=热门&page_limit=50&page_start=0'
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
param_year='//h1/span[2]/text()'
param_genre='//span[@property="v:genre"]/text()'
param_directors='//span[1]/span[@class="attrs"]/a/text()'
param_scenarist='//span[2]/span[@class="attrs"]/a/text()'
param_actors='//span[text()="主演"]/following::span[@class="attrs"]/a/text()'
param_country='//span[text()="制片国家/地区:"]/following::text()[1]'
def get(l,i,url):
	res=requests.get(url,headers=headers)
	res.encoding='utf8'
	tree=etree.HTML(res.text)
	# print(res.text)
	# print(tree)
	l[i]['year']=int(tree.xpath(param_year)[0][1:5])
	l[i]['genre']=tree.xpath(param_genre)
	l[i]['actors']=tree.xpath(param_actors)
	# print(l[i]['actors'])
	# print(' / '.join(l[i]['actors']))
	l[i]['directors']=tree.xpath(param_directors)[0]
	l[i]['scenarist']=tree.xpath(param_scenarist)[0]
	l[i]['name']=l[i]['title']
	l[i]['star']=l[i]['rate']
	ss=f"导演：{l[i]['directors']}；编剧：{l[i]['scenarist']}；主演：{' / '.join(l[i]['actors'])}"
	l[i]['actor']=ss
	l[i]['country']=tree.xpath(param_country)[0][1:]
	ss=""
	l[i]['type']=f"{l[i]['year']} / {l[i]['country']} / {' '.join(l[i]['genre'])}"
	return

resp=requests.get(home,headers=headers)
resp.encoding='utf8'
list=json.loads(resp.text)['subjects']

for i in range(len(list)):
# for i in range(1):
	try:
		del list[i]["episodes_info"]
		del list[i]["cover_x"]
		del list[i]["cover_y"]
		del list[i]["playable"]
		del list[i]["cover"]
		del list[i]["id"]
		del list[i]["is_new"]
		print(f'id = {i}',end=' ')
		get(list,i,list[i]['url'])
		print('succeed')
		sleep(1)
		
	except KeyboardInterrupt as e:
		exit(0)
	except Exception as e:
		print(f"err occurs, err:{e}")
with open("list.json","w",encoding='utf8') as fp:
	json.dump(list,fp,ensure_ascii=False)