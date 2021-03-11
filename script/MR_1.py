# coding=utf-8
#from translate_google import *
import selenium
from translate_baidu import *
from functions import *
import numpy as np
import pandas as pd
import time
#import simplejson

url = 'https://www.fakerfact.org/'
url_try = 'https://www.fakerfact.org/try-it-out'

source = pd.read_csv('../reason_lists.csv', encoding='utf-8')
followup = pd.read_csv('../similarity.csv', encoding='utf-8')


source_sentences = source[source.columns[1]].values.tolist()[3300:3500]
#source_labels = source[source.columns[2]].values.tolist()[5:50]
old_sentences = []
source_labels = []
followup_sentences = followup[followup.columns[1]].values.tolist()[3300:3500]
new_sentences = []
followup_labels = []

def MR_1(browser):

	consistence = 0
	total = len(followup_sentences)
	index = 0

	# go to fakerfact website
	browser.get(url_try)

	for i in range(len(followup_sentences)):
		print(source_sentences[i])
		print()
		print()
		print(followup_sentences[i])
		print()
		print()
		index += 1
		if type(followup_sentences[i]) != str:
			total -= 1
			print('Empty follow up sentence')
		else:

			try:
				# enter the sentences (as input)
				time.sleep(2)
				input_box = browser.find_element_by_class_name('form-control')
				input_box.send_keys(source_sentences[i])
				input_box.submit()

				# get the output
				time.sleep(4)
				output_s = print_label(browser.find_element_by_class_name('ff-flag').text)				

				# go back to 'try-it-out' page
				time.sleep(2)
				browser.get(url_try)

				time.sleep(2)
				input_box = browser.find_element_by_class_name('form-control')
				input_box.send_keys(followup_sentences[i])
				input_box.submit()

				# get the output
				time.sleep(4)
				output_f = print_label(browser.find_element_by_class_name('ff-flag').text)				

				print('Number ', index)
				print('Source test case: ', output_s)
				print('Follow-up test case: ', output_f)

				if str(output_s) == str(output_f):
					consistence += 1
					print('The result correpsonds with the MR')
				else:
					print('The result does not correspond with the MR')
				print('----------')
				old_sentences.append(source_sentences[i])
				new_sentences.append(followup_sentences[i])
				source_labels.append(output_s)
				followup_labels.append(output_f)
				# go back to 'try-it-out' page
				time.sleep(2)
				browser.get(url_try)

			except selenium.common.exceptions.NoSuchElementException:
				print('**Something goes wrong**')
				total -= 1
				time.sleep(2)
				browser.get(url_try)

	rate = consistence / total
	print('The total pass rate is ', rate)
	print('Correct number is ', consistence)
	print('Total number is ', total)

	reason_file = pd.DataFrame({
		'Reason Lists': old_sentences,
		'Labels': source_labels
		})
	reason_file.to_csv('../old3300_3500.csv', encoding='utf-8')

	reason_file = pd.DataFrame({
		'Reason Lists': new_sentences,
		'Labels': followup_labels
		})
	reason_file.to_csv('../new3300_3500.csv', encoding='utf-8')







	# #Baidu back translation 
	# #google_tokn = GoogleToken()
	# successed = []
	# failed = []
	# index = 0

	# try:
	# 	for i in range(len(sentences)):	
	# 		index += 1

	# 		temp = translate_baidu('en', 'zh', sentences[i])
	# 		time.sleep(1)
	# 		text_translate = translate_baidu('zh', 'en', temp)
	# 		time.sleep(1)

	# 		if sentences[i] != text_translate:
	# 				print('Successful ', index)
	# 				successed.append(text_translate)
	# 		else:
	# 			print('Failure ', index)
	# 			failed.append(text_translate)
			
	# except TypeError:
	# 	print('Something went wrong')


	# # Google back translation
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


			
	# success = pd.DataFrame({
	# 	'Similar sentences': successed,
	# 	'Labels': np.nan
	# 	})
	# success.to_csv('../similarity11500_baidu.csv', encoding='utf-8')

	# failure = pd.DataFrame({
	# 	'Similar sentences': failed,
	# 	'Labels': np.nan
	# 	})
	# failure.to_csv('../failure11500_baidu.csv', encoding='utf-8')




