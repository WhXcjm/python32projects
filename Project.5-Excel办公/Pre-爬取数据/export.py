# pip install pandas
import pandas as pd
import json
pd.set_option("display.max_rows",5)
pd.set_option('display.max_columns',None)

with open("list.json","r",encoding='utf8') as f:
	raw1=json.load(f)
raw2=[]
headers=['name','star','actor','type']
for item in raw1:
	# try:
	tmp=[item[key] for key in headers]
	# print(tmp)
	# except KeyboardInterrupt:
	# 	exit(0)
	# except Exception as e:
	# 	print(f"err: {e}")
	raw2.append(tmp)
data=pd.DataFrame(raw2,columns=headers)
print(data)