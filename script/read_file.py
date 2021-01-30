# coding=utf-8
import pandas as pd 
import urllib.request
import time
import http
from random import randint

def read_csv(file_name):
	opener = urllib.request.build_opener()
	#headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
	#random_agent = USER_AGENTS[randint(0, len(USER_AGENTS)-1)]

	opener.addheaders = [('User-agent', 'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3')]
	data = pd.read_csv(file_name)
	workable = []

	for url in data['news_url']:
		tempUrl = str(url)
		if 'www' in tempUrl:
		#if 'http' in tempUrl:
			try:
				#res = urllib.request.Request(tempUrl, headers=headers)
				opener.open(tempUrl)
				#urllib.request.urlopen(res).read()
				print('OK')
				workable.append(tempUrl)
			except urllib.error.HTTPError:
				print('Error')
				time.sleep(2)
			except urllib.error.URLError:
				print('Error')
				time.sleep(2)
			except http.client.HTTPException:
				print('timeout. URL is ', tempUrl)
				time.sleep(2)
			time.sleep(0.1)

	name = ['URL']
	workable_csv = pd.DataFrame(columns=name, data=workable)
	workable_csv.to_csv('../workable_url1.csv', encoding='gbk')
	# for url in data['news_url']:
	# 	with request.urlopen(url) as file:
	# 		print(file.status)

def joint_files(workable1, workable2):
	data1 = pd.read_csv(workable1)['news_url']
	data2 = pd.read_csv(workable2)['news_url']
	result = data1.append(data2).reset_index(drop=True)
	name = ['news_url']
	result = pd.DataFrame(columns=name, data=result)
	result.to_csv('../safe_url.csv', encoding='utf-8')



