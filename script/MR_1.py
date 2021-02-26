# coding=utf-8
#from translate_google import *
from translate_baidu import *
import numpy as np
import pandas as pd
import time
#import simplejson


def MR_1(sentences, labels):	

	#google_tokn = GoogleToken()
	successed = []
	failed = []
	index = 0

	try:
		for i in range(len(sentences)):	
			index += 1

			temp = translate_baidu('en', 'zh', sentences[i])
			time.sleep(1)
			text_translate = translate_baidu('zh', 'en', temp)
			time.sleep(1)

			if sentences[i] != text_translate:
					print('Successful ', index)
					successed.append(text_translate)
			else:
				print('Failure ', index)
				failed.append(text_translate)
			
	except TypeError:
		print('Something went wrong')


	# try:
	# 	for i in range(len(sentences)):	
	# 		index += 1
	# 		#print(sentences[i])
	# 		#print('----------------------------------------------------------')
	# 		text_translate_google = any_to_any_translate_back(sentences[i], google_tokn, from_='en', to_='zh-CN')
	# 		#print(text_translate)
	# 		if sentences[i] != text_translate_google:
	# 			#print('Successful ', index)
	# 			successed.append(text_translate_google)
	# 		else:
	# 			#print('Failure ', index)
	# 			failed.append(text_translate_google)
	# except simplejson.errors.JSONDecodeError:
	# 	print('Something went wrong')


			
	success = pd.DataFrame({
		'Similar sentences': successed,
		'Labels': np.nan
		})
	success.to_csv('../similarity75008000_baidu.csv', encoding='utf-8')

	failure = pd.DataFrame({
		'Similar sentences': failed,
		'Labels': np.nan
		})
	failure.to_csv('../failure75008000_baidu.csv', encoding='utf-8')




