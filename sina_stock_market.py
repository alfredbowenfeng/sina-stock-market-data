#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import urllib.request
import csv
baseUrl = "http://hq.sinajs.cn/list="
szUrl = "sz"
shUrl = "sh"
sz1 = "00000"
sz2 = "0000"
sz3 = "000"
sz4 = "00"
F = ""
F1 = ""
F2 = ""
F3 = ""
F4 = ""
F5 = ""
F6 = ""
_session = requests.session()

# 000001-000009
for i in range(1,10):
    j = str(i)
    stockUrl = baseUrl + szUrl + sz1 + j
    content = _session.get(stockUrl).content
    stock = content.decode('gbk')[13:]
    if len(stock) > 11:
        F11 = stock[-1]
        F12 = stock[0:6] + ","
        F13 = stock[8:-3]
        F1 += F11 + F12 + F13
    else:
        pass

# 000010-000099
for i in range(10,100):
	j = str(i)
	stockUrl = baseUrl + szUrl + sz2 + j
	content = _session.get(stockUrl).content
	stock = content.decode('gbk')[13:]
	if len(stock) > 11:
		F21 = stock[-1]
		F22 = stock[0:6] + ","
		F23 = stock[8:-3]
		F2 += F21 + F22 + F23
	else:
		pass

# 000100-000999
for i in range(100,1000):
	j = str(i)
	stockUrl = baseUrl + szUrl + sz3 + j
	content = _session.get(stockUrl).content
	stock = content.decode('gbk')[13:]
	if len(stock) > 11:
		F31 = stock[-1]
		F32 = stock[0:6] + ","
		F33 = stock[8:-3]
		F3 += F31 + F32 + F33
	else:
		pass

# 001000-002999
for i in range(1000,3000):
	j = str(i)
	stockUrl = baseUrl + szUrl + sz4 + j
	content = _session.get(stockUrl).content
	stock = content.decode('gbk')[13:]
	if len(stock) > 11:
		F41 = stock[-1]
		F42 = stock[0:6] + ","
		F43 = stock[8:-3]
		F4 += F41 + F42 + F43
	else:
		pass

# 300001-300999
for i in range(300001,301000):
	j = str(i)
	stockUrl = baseUrl + szUrl + j
	content = _session.get(stockUrl).content
	stock = content.decode('gbk')[13:]
	if len(stock) > 11:
		F51 = stock[-1]
		F52 = stock[0:6] + ","
		F53 = stock[8:-3]
		F5 += F51 + F52 + F53
	else:
		pass

600001-604999
for i in range(600001,605000):
	j = str(i)
	stockUrl = baseUrl + shUrl + j
	content = _session.get(stockUrl).content
	stock = content.decode('gbk')[13:]
	if len(stock) > 11:
		F61 = stock[-1]
		F62 = stock[0:6] + ","
		F63 = stock[8:-3]
		F6 += F61 + F62 + F63
	else:
		pass

F = F1 + F2 + F3 + F4 + F5 + F6
print(F)