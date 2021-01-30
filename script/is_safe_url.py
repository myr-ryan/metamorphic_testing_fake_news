# coding=utf-8
from django.utils.http import is_safe_url
import pandas as pd 
import requests
import urllib3

# def check_safety(filename):
# 	data = pd.read_csv(filename)
# 	safe_url = []

# 	for url in data['news_url']:
# 		tempUrl = str(url)
# 		if not tempUrl == 'nan':
# 			if is_safe_url(tempUrl, allowed_hosts='www.youtube.com'):
# 				#print('This url is safe')
# 				safe_url.append(tempUrl)
# 			else:
# 				print('This url is risky: ', tempUrl)


# 	name = ['news_url']
# 	safe_csv = pd.DataFrame(columns=name, data=safe_url)
# 	safe_csv.to_csv('../safe_url1.csv', encoding='utf-8')

key = 'AIzaSyBZZ7tN83YYztM8KH9t6CH1YRQVcnnX6Ec'
URL = "https://sb-ssl.google.com/safebrowsing/api/lookup?client=api&apikey={key}&appver=1.0&pver=3.0&url={url}"
urllib3.disable_warnings()

def check_safety(filename):
	data = pd.read_csv(filename)
	safe_url = []
	malware = 0
	index = 0

	for url in data['news_url'][16000::]:
		tempUrl = str(url)
		if not tempUrl == 'nan':
			resp = requests.get(URL.format(key=key, url=tempUrl), verify=False)

			if resp.text != 'malware':
				print('Safe ', index)
				safe_url.append(tempUrl)
			else:
				print('This url is harmful: ', tempUrl)
				malware += 0
		index += 1


	print('Harmful url number: ', malware)
	name = ['news_url']
	safe_csv = pd.DataFrame(columns=name, data=safe_url)
	safe_csv.to_csv('../safe_url1.csv', encoding='utf-8')
	#for url in data['news_url']:
		



