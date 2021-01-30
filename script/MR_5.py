# coding=utf-8
import numpy as np
from functions import *
import time
import selenium
import random


url = 'https://www.fakerfact.org/'
url_try = 'https://www.fakerfact.org/try-it-out'

def perm(sentences):
	splited = sentences.split('\n')
	splited_new = []
	for s in splited:
		s_temp = s[1:len(s)-1].split(' ')
		random.shuffle(s_temp)
		splited_new.append('"' + ' '.join(s_temp) + '"')

	return splited_new




def MR_5(browser, sentences, labels):

	consistence = 0
	total = len(sentences)

	# go to fakerfact website
	browser.get(url_try)

	for i in range(len(sentences)):
		try:
			# enter the sentences (as input)
			time.sleep(2)
			input_box = browser.find_element_by_class_name('form-control')
			input_box.send_keys(perm(sentences[i]))
			input_box.submit()

			# get the output
			time.sleep(4)
			output = print_label(browser.find_element_by_class_name('ff-flag').text)
			print('Source test case: ', labels[i])
			print('Follow-up test case: ', output)

			if str(labels[i]) == str(output):
				consistence += 1
				print('The result correpsonds with the MR')
			else:
				print('The result does not correspond with the MR')
			print('----------')
			# go back to 'try-it-out' page
			time.sleep(2)
			browser.get(url_try)

		except selenium.common.exceptions.NoSuchElementException:
			print('**Something goes wrong**')
			total -= 1
			time.sleep(2)
			browser.get(url_try)

	rate = consistence / total
	print('The total pass rate is ', 1 - rate)
	print('Correct number is ', consistence)
	print('Total number is ', total)


