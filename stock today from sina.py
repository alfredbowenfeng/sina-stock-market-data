#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import urllib.request
import pandas as pd
stock,baseUrl = "","http://hq.sinajs.cn/list="
List1,List2,List3,List4,List5,List6,List7,List8 = [],[],[],[],[],[],[],[]
_session = requests.session()

def genUrl(x):
	stockID = str(x)
	if x >=10:
		if x >= 100:
			if x >= 1000:
				if x >= 3000:
					if x >= 300000:
						if x >= 300740:
							if x >= 600000:
								stockUrl = baseUrl + "sh" + stockID
								getPage(stockUrl)
							else:
								pass
						else:
							stockUrl = baseUrl + "sz" + stockID
							getPage(stockUrl)
					else:
						pass
				else:
					stockUrl = baseUrl + "sz00" + stockID
					getPage(stockUrl)
			else:
				stockUrl = baseUrl + "sz000" + stockID
				getPage(stockUrl)
		else:
			stockUrl = baseUrl + "sz0000" + stockID
			getPage(stockUrl)
	else:
		stockUrl = baseUrl + "sz00000" + stockID
		getPage(stockUrl)

def getPage(u):
	global stock
	content = _session.get(u).content
	content = content.decode('gbk')[13:]
	if len(content) > 11:
		stock = content[0:6] + "," + content[8:-6]
		element = stock.split(",")
		List1.append(element[0])
		List2.append(element[1])
		List3.append(element[2])
		List4.append(element[3])
		List5.append(element[4])
		List6.append(element[5])
		List7.append(element[6])
		List8.append(element[-2])
	else:
		pass

for i in range(1,604000):
	genUrl(i)

# Export data
dataframe = pd.DataFrame({"股票代码":List1,"股票名称":List2,"今日开盘价":List3,"昨日收盘价":List4,"今日收盘价":List5,"今日最高价":List6,"今日最低价":List7,"日期":List8})
dataframe.to_csv('/data.csv',index=False,sep=',',encoding="utf-8")